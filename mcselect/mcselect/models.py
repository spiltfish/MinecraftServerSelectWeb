from django.db import models
import uuid

class Server(models.Model):
    server_name = models.CharField(max_length=128, unique=True, default=uuid.uuid1)
    is_enabled = models.BooleanField()
    server_type = models.CharField(max_length=128)
    server_version = models.CharField(max_length=128)
    is_deployed = models.BooleanField(default=False)

    @classmethod
    def create(cls, server_name, server_type, server_version):
        server = cls(server_name=server_name, is_enabled=False, server_type=server_type, server_version=server_version,
                     is_deployed=False)
        return server

    def __unicode__(self):
        return '{}@{}'.format(self.sever_name, self.is_enabled)

    def __str__(self):
        return '{}@{}'.format(self.sever_name, self.is_enabled)