# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0018_delete_analyze_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyze_job_status',
            name='rp_t_status',
            field=models.CharField(max_length=10, default='pending'),
        ),
    ]
