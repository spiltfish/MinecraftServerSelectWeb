from django.views.generic import TemplateView
from django.db import transaction
from django.http import HttpResponseRedirect
from mcselect.models import Server
from mcselect.server_actions.set_up_new_server import set_up_new_ftb_server

class ServerSelectView(TemplateView):
    template_name = 'servers-select.html'

    def get_context_data(self, **kwargs):
        context = super(ServerSelectView, self).get_context_data(**kwargs)
        context["all_servers"] = Server.objects.all()
        return context


class AddServer(TemplateView):
    template_name = 'server-add.html'

    def get_context_data(self, **kwargs):
        context = super(AddServer, self).get_context_data(**kwargs)
        #context["new_server"] = Server.create()

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            print("Creating new server.")
            print(request.POST.get("name", ""))
            print(args)
            print(kwargs)
            server = Server.create(request.POST.get("name", ""), "server_type", "server_version")
            server.save()


        return HttpResponseRedirect("/")