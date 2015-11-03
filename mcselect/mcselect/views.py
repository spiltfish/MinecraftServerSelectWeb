from django.views.generic import TemplateView, CreateView, ListView

from mcselect.forms import AddServerForm
from mcselect.models import Server


class ServerSelectView(ListView):
    template_name = 'servers-select.html'
    model = Server


class AddServer(CreateView):
    template_name = 'server-add.html'
    form_class = AddServerForm
