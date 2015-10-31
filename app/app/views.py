from django.views.generic import TemplateView


class ServerSelectView(TemplateView):
    template_name = 'server_select.html'

    def get_context_data(self, **kwargs):
        context = super(ServerSelectView, self).get_context_data()
        return context

def add_server(request):
    if request.method == 'POST':
