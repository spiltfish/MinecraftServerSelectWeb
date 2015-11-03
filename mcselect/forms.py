from django.forms import ModelForm, Form
from django.forms import CharField, FileField
from mcselect.models import Server
from django.utils.translation import ugettext as _


class AddServerForm(ModelForm):
    """
    This Form Creates a New Server, and should then set up the server for the first time
    """

    class Meta:
        model = Server
        fields = ["name", "type", "version"]
        help_texts = {
            'version': _('Minecraft Server version'),
            'type': _('The type of server'),
        }


class UploadServerZipForm(Form):
    title = CharField(max_length=50)
    file = FileField()
