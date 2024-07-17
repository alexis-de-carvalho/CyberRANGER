from flask_babel import lazy_gettext as _l
from wtforms import BooleanField, PasswordField, SelectField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired

from CTFd.constants.config import Configs
from CTFd.constants.languages import SELECT_LANGUAGE_LIST
from CTFd.forms import BaseForm
from CTFd.forms.fields import SubmitField
#from CTFd.models import Brackets, InstanceFieldEntries, InstanceFields
from CTFd.utils.countries import SELECT_COUNTRIES_LIST




class InstanceSearchForm(BaseForm):
    field = SelectField(
        "Search Field",
        choices=[
            ("network", "Network"),
            ("value", "Value"),
            ("challenge_id", "Challenge ID"),
            ("status", "Status"),
            ("ip", "IP"),
        ],
        default="network",
        validators=[InputRequired()],
    )
    q = StringField("Parameter", validators=[InputRequired()])
    submit = SubmitField("Search")


class PublicInstanceSearchForm(BaseForm):
    field = SelectField(
        _l("Search Field"),
        choices=[
            ("network", _l("Network")),
            ("value", _l("Value")),
            ("challenge_id", _l("Challenge ID")),
        ],
        default="network",
        validators=[InputRequired()],
    )
    q = StringField(
        _l("Parameter"),
        description=_l("Search for matching instances"),
        validators=[InputRequired()],
    )
    submit = SubmitField(_l("Search"))


class InstanceBaseForm(BaseForm):
    network = StringField("Network", validators=[InputRequired()])
    value = StringField("Value", validators=[InputRequired()])
    challenge_id = StringField("Challenge ID", validators=[InputRequired()])
    submit = SubmitField("Submit")




def InstanceEditForm(*args, **kwargs):
    class _InstanceEditForm(InstanceBaseForm):
        pass

        def __init__(self, *args, **kwargs):
            """
            Custom init to persist the obj parameter to the rest of the form
            """
            super().__init__(*args, **kwargs)
            obj = kwargs.get("obj")
            if obj:
                self.obj = obj

    return _InstanceEditForm(*args, **kwargs)


def InstanceCreateForm(*args, **kwargs):
    class _InstanceCreateForm(InstanceBaseForm):
        notify = BooleanField("Email account credentials to instance", default=True)

    return _InstanceCreateForm(*args, **kwargs)
