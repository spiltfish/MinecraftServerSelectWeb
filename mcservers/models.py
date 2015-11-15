import uuid

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _


class Server(models.Model):
    name = models.CharField(_('Server Name'), max_length=128)
    uuid = models.SlugField(_('Unique Identifier'), unique=True, default=uuid.uuid4, editable=False)
    is_enabled = models.BooleanField(default=True)
    type = models.CharField(max_length=128)
    version = models.CharField(max_length=128)
    is_deployed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('mcservers:server-detail', args=(self.id,))

    def __unicode__(self):
        return '{}@{}'.format(self.sever_name, self.is_enabled)

    def __str__(self):
        return '{}@{}'.format(self.sever_name, self.is_enabled)


class Modpack(models.Model):
    name = models.CharField(_('Modpack Name'), max_length=128)
    uuid = models.SlugField(_('Unique Identifier'), unique=True, default=uuid.uuid4, editable=False)
    version = models.CharField(max_length=128)
    file = models.FileField(name=name)


class Mod(models.Model):
    name = models.CharField(_('Mod Name'), max_length=128)
    uuid = models.SlugField(_('Unique Identifier'), unique=True, default=uuid.uuid4, editable=False)
    version = models.CharField(max_length=128)
    file = models.FileField(name=name)

class SeverInstallationProcedure(models.Model):
    pass

class ProcedureStep(models.Model):
    name = models.CharField(_('Step Name'), max_length=128)
    description = models.CharField(_('Step Description'), max_length=128)