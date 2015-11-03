# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Server Name', max_length=128)),
                ('uuid', models.SlugField(editable=False, verbose_name='Unique Identifier', unique=True, default=uuid.uuid4)),
                ('is_enabled', models.BooleanField(default=True)),
                ('type', models.CharField(max_length=128)),
                ('version', models.CharField(max_length=128)),
                ('is_deployed', models.BooleanField(default=False)),
            ],
        ),
    ]
