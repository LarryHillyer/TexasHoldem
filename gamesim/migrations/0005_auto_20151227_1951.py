# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0004_simulation_job_summary_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulation_job',
            name='run_time',
            field=models.DateTimeField(null=True),
        ),
    ]
