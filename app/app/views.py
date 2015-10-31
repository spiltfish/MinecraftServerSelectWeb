from django.views.generic import TemplateView
from django.db import transaction
from django.http import HttpResponseRedirect
from app.models.server import Server

class ServerSelectView(TemplateView):
    template_name = 'servers-select.html'

    def get_context_data(self, **kwargs):
        context = super(ServerSelectView, self).get_context_data()
        return context

class AddServer(TemplateView):
    template_name = 'server-add.html'

    def post(self, request, *args, **kwargs):
        if 'add_server' in request.POST:
            with transaction.atomic():
                server = Server.objects()

                server.save()

        return HttpResponseRedirect("/server-select.html")