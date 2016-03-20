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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('url_image', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=60)),
                ('cupo_max', models.PositiveSmallIntegerField()),
                ('cupo_disp', models.PositiveSmallIntegerField()),
                ('date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('asistentes', models.PositiveSmallIntegerField()),
                ('event', models.ForeignKey(related_name='reservations', to='api.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
