from marshmallow import ValidationError, post_dump, pre_load, validate
from marshmallow.fields import Nested
from marshmallow_sqlalchemy import field_for
from sqlalchemy.orm import load_only

from CTFd.models import Instances, ma
#from CTFd.schemas.fields import UserFieldEntriesSchema
from CTFd.utils import get_config, string_types
from CTFd.utils.crypto import verify_password
from CTFd.utils.email import check_email_is_whitelisted
from CTFd.utils.user import get_current_user, is_admin
from CTFd.utils.validators import validate_country_code, validate_language


class InstanceSchema(ma.ModelSchema):
    class Meta:
        model = Instances
        include_fk = True
        dump_only = ("id")
        load_only = ("password",)

    network = field_for(Instances, "network")
    value = field_for(Instances, "value")
    ip = field_for(Instances, "ip")
    status = field_for(Instances, "status")
    challenge_id = field_for(Instances, "challenge_id")
    
    views = {
        "user": [
            "network",
            "value",
            "ip",
            "status",
            "challenge_id",
        ],
        "self": [
            "network",
            "value",
            "ip",
            "status",
            "challenge_id",
        ],
        "admin": [
            "network",
            "value",
            "ip",
            "status",
            "challenge_id",
        ],
    }
    

    def __init__(self, view=None, *args, **kwargs):
        if view:
            if isinstance(view, string_types):
                kwargs["only"] = self.views[view]
            elif isinstance(view, list):
                kwargs["only"] = view
        self.view = view

        super(InstanceSchema, self).__init__(*args, **kwargs)
