import os

from typing import List

from flask import abort, request, session
from flask_restx import Namespace, Resource

from CTFd.api.v1.helpers.request import validate_args
from CTFd.api.v1.helpers.schemas import sqlalchemy_to_pydantic
from CTFd.api.v1.schemas import (
    APIDetailedSuccessResponse,
    PaginatedAPIListSuccessResponse,
)
from CTFd.cache import clear_challenges, clear_standings
from CTFd.constants import RawEnum
from CTFd.models import (
    Awards,
    Notifications,
    Solves,
    Submissions,
    Tracking,
    Unlocks,
    Instances,
    db,
)
from CTFd.schemas.awards import AwardSchema
from CTFd.schemas.submissions import SubmissionSchema
from CTFd.schemas.instances import InstanceSchema
from CTFd.utils.config import get_mail_provider
from CTFd.utils.decorators import admins_only, authed_only, ratelimit
from CTFd.utils.decorators.visibility import (
    check_account_visibility,
    check_score_visibility,
)
from CTFd.utils.email import sendmail
from CTFd.utils.helpers.models import build_model_filters
from CTFd.utils.user import is_admin

from CTFd.utils import get_app_config


instances_namespace = Namespace("instances", description="Endpoint to retrieve Instances")


def strip_url(url, character):

    index = url.find(character)
    if index != -1:
        return url[index+1:]
    return url

DATABASE_URL = get_app_config("SQLALCHEMY_DATABASE_URI")
DATABASE_URL = strip_url(DATABASE_URL, ':')


InstanceModel = sqlalchemy_to_pydantic(Instances)
TransientInstanceModel = sqlalchemy_to_pydantic(Instances, exclude=["id"])


class InstanceDetailedSuccessResponse(APIDetailedSuccessResponse):
    data: InstanceModel


class InstanceListSuccessResponse(PaginatedAPIListSuccessResponse):
    data: List[InstanceModel]


instances_namespace.schema_model(
    "InstanceDetailedSuccessResponse", InstanceDetailedSuccessResponse.apidoc()
)

instances_namespace.schema_model(
    "InstanceListSuccessResponse", InstanceListSuccessResponse.apidoc()
)



@instances_namespace.route("")
class InstancesList(Resource):
    @check_account_visibility    
    @validate_args(
        {
            "q": (str, None),
        },
        location="query",
    )
    
    def get(self, query_args):

        print("INSTANCES GETTTTTTT")

        q = query_args.pop("q", None)
        field = str(query_args.pop("field", None))

        filters = build_model_filters(model=Instances, query=q, field=field)

        if is_admin() and request.args.get("view") == "admin":
            instances = (
                Instances.query.filter_by(**query_args)
                .filter(*filters)
                .paginate(per_page=50, max_per_page=100)
            )
        else:
            instances = (
                Instances.query.filter_by(**query_args)
                .filter(*filters)
                .paginate(per_page=50, max_per_page=100)
            )

        response = InstanceSchema(many=True).dump(instances.items)

        if response.errors:
            return {"success": False, "errors": response.errors}, 400

        return {
            "meta": {
                "pagination": {
                    "page": instances.page,
                    "next": instances.next_num,
                    "prev": instances.prev_num,
                    "pages": instances.pages,
                    "per_page": instances.per_page,
                    "total": instances.total,
                }
            },
            "success": True,
            "data": response.data,
        }

    @admins_only
    def post(self):

        req = request.get_json()
        schema = InstanceSchema("admin")
        response = schema.load(req)

        if response.errors:
            return {"success": False, "errors": response.errors}, 400

        db.session.add(response.data)
        db.session.commit()

        response = schema.dump(response.data)

        return {"success": True, "data": response.data}




def createInstance(instance_id):
    instance = Instances.query.filter_by(id=instance_id).first_or_404()
    network = instance.network
    command = 'ansible-playbook -e "network_name={network} instance_id={instance_id} db_url={DATABASE_URL}" ./deploy/create.yml'.format(network=network,instance_id=instance_id,DATABASE_URL=DATABASE_URL)
    os.system(command)

    
def deleteInstance(instance_id):
    instance = Instances.query.filter_by(id=instance_id).first_or_404()
    network = instance.network
    command = 'ansible-playbook -e "network_name={network} instance_id={instance_id} db_url={DATABASE_URL}" ./deploy/destroy.yml'.format(network=network,instance_id=instance_id,DATABASE_URL=DATABASE_URL)
    os.system(command)



@instances_namespace.route("/create")
class InstancesCreate(Resource):
    @admins_only
    def post(self):

        data = request.json
        id_received = data.get('id')
        createInstance(id_received)

        return {"success": True}


@instances_namespace.route("/delete")
class InstancesDelete(Resource):

    @admins_only
    def post(self):

        data = request.json
        id_received = data.get('id')
        deleteInstance(id_received)

        return {"success": True}

