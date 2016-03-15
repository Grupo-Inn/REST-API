# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.TextField()),
                ('url_image', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=20)),
                ('lugar', models.CharField(max_length=60)),
                ('cupo_max', models.PositiveSmallIntegerField()),
                ('fecha', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
