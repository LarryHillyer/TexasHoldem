# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0012_finished_jobs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finished_jobs',
            name='finished_job_list',
        ),
    ]
