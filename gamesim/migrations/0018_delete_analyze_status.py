# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0017_analyze_job_status_analyze_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='analyze_status',
        ),
    ]
