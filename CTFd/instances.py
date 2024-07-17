from flask import Blueprint, render_template, request, url_for

from CTFd.models import Instances
from CTFd.utils import config
from CTFd.utils.decorators import authed_only
from CTFd.utils.decorators.visibility import (
    check_account_visibility,
    check_score_visibility,
)
from CTFd.utils.helpers import get_errors, get_infos

instances = Blueprint("instances", __name__)


@instances.route("/instances")
@check_account_visibility
def listing():
    
    q = request.args.get("q")
    field = request.args.get("field")
    page = abs(request.args.get("page", 1, type=int))
    filters = []
    instances = []

    if q:
        # The field exists as an exposed column
        if Instances.__mapper__.has_property(field):
            filters.append(getattr(Instances, field).like("%{}%".format(q)))

    else:
        instances = (
            Instances.query.filter(*filters)
            .order_by(Instances.id.asc())
            .paginate(page=page, per_page=50)
        )

    args = dict(request.args)
    args.pop("page", 1)

    return render_template(
        "instances/instances.html",
        instances=instances,
        prev_page=url_for(request.endpoint, page=instances.prev_num, **args),
        next_page=url_for(request.endpoint, page=instances.next_num, **args),
        q=q,
        field=field,
    )
