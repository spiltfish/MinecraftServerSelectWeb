from django.db import models
import uuid
from django.utils.translation import ugettext as _


class Server(models.Model):
    name = models.CharField(_('Server Name'), max_length=128)
    uuid = models.SlugField(_('Unique Identifier'), unique=True, default=uuid.uuid4, editable=False)
    is_enabled = models.BooleanField(default=True)
    type = models.CharField(max_length=128)
    version = models.CharField(max_length=128)
    is_deployed = models.BooleanField(default=False)

    def __unicode__(self):
        return '{}@{}'.format(self.sever_name, self.is_enabled)

    def __str__(self):
        return '{}@{}'.format(self.sever_name, self.is_enabled)
