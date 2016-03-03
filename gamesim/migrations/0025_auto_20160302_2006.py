# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0024_auto_20160103_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyzed_jobs',
            name='sim_dir',
            field=models.CharField(max_length=200, default='C:\\Users\\Larry\\SkyDrive\\Python\\Django\\TexasHoldem\\gamesim\\sim_scripts\\'),
        ),
        migrations.AlterField(
            model_name='finished_jobs',
            name='sim_dir',
            field=models.CharField(max_length=200, default='C:\\Users\\Larry\\SkyDrive\\Python\\Django\\TexasHoldem\\gamesim\\sim_scripts\\'),
        ),
        migrations.AlterField(
            model_name='simulation_job',
            name='sim_dir',
            field=models.CharField(max_length=200, default='C:\\Users\\Larry\\SkyDrive\\Python\\Django\\TexasHoldem\\gamesim\\sim_scripts\\'),
        ),
    ]
