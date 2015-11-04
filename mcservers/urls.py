from django.conf.urls import url

from mcservers.views import ServerDetailView
from .views import ServerListView, AddServerCreateView

urlpatterns = [
    url(r'^$', ServerListView.as_view(), name='server-list'),
    url(r'^(?P<pk>[0-9]+)', ServerDetailView.as_view(), name='server-detail'),
    url(r'^add/$', AddServerCreateView.as_view(), name='server-create'),
]