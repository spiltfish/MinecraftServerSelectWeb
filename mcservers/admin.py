from django.contrib import admin
from .models import Server, Mod, Modpack
# Register your models here.
admin.site.register((Server, Mod, Modpack))