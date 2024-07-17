from flask import render_template, request, url_for, jsonify
from sqlalchemy.sql import not_

from CTFd.admin import admin
from CTFd.models import Challenges, Tracking, Instances
from CTFd.utils import get_config
from CTFd.utils.decorators import admins_only
from CTFd.utils.modes import TEAMS_MODE


@admin.route("/admin/instances")
@admins_only
def instances_listing():

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
        "admin/instances/instances.html",
        instances=instances,
        prev_page=url_for(request.endpoint, page=instances.prev_num, **args),
        next_page=url_for(request.endpoint, page=instances.next_num, **args),
        q=q,
        field=field,
    )


@admin.route("/admin/instances/new")
@admins_only
def instances_new():
    return render_template("admin/instances/new.html")


@admin.route("/admin/instances/<int:instance_id>")
@admins_only
def instances_detail(instance_id):
    # Get instance object
    instance = Instances.query.filter_by(id=instance_id).first_or_404()

    return render_template(
        "admin/instances/instance.html",
        instance=instance,
    )

