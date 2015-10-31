from django import forms

class AddServerForm(forms.Form):
    '''This Form Creates a New Server, and should then set up the server for the first time'''
    server_name = forms.CharField(label='Server Name', max_length=50)
    #mod_pack = SelectField() # This should be a select field of all modpacks in the modpacks DB