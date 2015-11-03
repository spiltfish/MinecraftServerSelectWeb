from django.views.generic import CreateView, ListView, DetailView

from .forms import AddServerForm
from .models import Server


class ServerListView(ListView):
    model = Server


class ServerDetailView(DetailView):
    model = Server


class AddServerCreateView(CreateView):
    template_name = 'mcservers/server_create.html'
    form_class = AddServerForm
