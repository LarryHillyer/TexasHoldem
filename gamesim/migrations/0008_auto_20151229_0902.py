# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0007_simulation_job_save_game_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulation_job',
            name='save_game_data',
            field=models.BooleanField(default=False),
        ),
    ]
