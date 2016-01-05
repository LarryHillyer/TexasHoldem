# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0006_dispatcher_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulation_job',
            name='save_game_data',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
