from django.db import models

class Server(models.Model):
    sever_name = models.CharField(max_length=128)
    is_enabled = models.BooleanField()
    server_type = models.CharField(max_length=128)
    server_version = models.CharField(max_length=128)

    def __unicode__(self):
        return '{}@{}'.format(self.sever_name, self.is_enabled)

    def __str__(self):
        return '{}@{}'.format(self.sever_name, self.is_enabled)