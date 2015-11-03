from django.views.generic import CreateView, ListView

from mcselect.forms import AddServerForm
from mcselect.models import Server


class ServerListView(ListView):
    model = Server


class AddServerCreateView(CreateView):
    template_name = 'mcselect/server-create.html'
    form_class = AddServerForm
