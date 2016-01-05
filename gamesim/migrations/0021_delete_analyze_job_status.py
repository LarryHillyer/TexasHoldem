# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0020_analyze_job_status_p_cp_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='analyze_job_status',
        ),
    ]
