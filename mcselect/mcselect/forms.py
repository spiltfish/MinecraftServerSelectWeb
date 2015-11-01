from django.forms import ModelForm, Form
from django.forms import CharField, FileField
from mcselect.models import Server

class AddServerForm(ModelForm):
    '''This Form Creates a New Server, and should then set up the server for the first time'''
    class Meta:
        model = Server
        fields = ['server_name', "server_type", "server_version"]

class UploadServerZipForm(Form):
    title = CharField(max_length=50)
    file = FileField()