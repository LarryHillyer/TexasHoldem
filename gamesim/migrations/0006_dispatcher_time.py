# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0005_auto_20151227_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='dispatcher_time',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('time_delta', models.TimeField(null=True)),
            ],
        ),
    ]
