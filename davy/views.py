import logging

from django.views.generic import TemplateView

logger = logging.getLogger('davy')


class IndexView(TemplateView):
    template_name = 'index.html'
