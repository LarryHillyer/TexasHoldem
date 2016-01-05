# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0011_auto_20151229_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='finished_jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('finished_job_list', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
    ]
