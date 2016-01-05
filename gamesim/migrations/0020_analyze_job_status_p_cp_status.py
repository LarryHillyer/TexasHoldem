# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0019_analyze_job_status_rp_t_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyze_job_status',
            name='p_cp_status',
            field=models.CharField(max_length=10, default='pending'),
        ),
    ]
