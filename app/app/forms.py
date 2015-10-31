from django.forms import ModelForm
from app.models.server import Server

class AddServerForm(ModelForm):
    '''This Form Creates a New Server, and should then set up the server for the first time'''
    class Meta:
        model = Server
        fields = ['server_name', "server_type", "server_version"]