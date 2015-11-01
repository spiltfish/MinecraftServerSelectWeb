from django.db import models

class Server(models.Model):
    server_name = models.CharField(max_length=128)
    is_enabled = models.BooleanField()
    server_type = models.CharField(max_length=128)
    server_version = models.CharField(max_length=128)

    @classmethod
    def create(cls, server_name, server_type, server_version):
        print("server.create")
        server = cls(server_name=server_name, is_enabled=False, server_type=server_type, server_version=server_version)
        return server

    def __unicode__(self):
        return '{}@{}'.format(self.sever_name, self.is_enabled)

    def __str__(self):
        return '{}@{}'.format(self.sever_name, self.is_enabled)