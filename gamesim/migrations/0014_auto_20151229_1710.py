# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0013_remove_finished_jobs_finished_job_list'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='finished_jobs',
            options={'ordering': ('run_time',)},
        ),
        migrations.AddField(
            model_name='finished_jobs',
            name='finish_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='finished_jobs',
            name='job_name',
            field=models.CharField(null=True, max_length=30, unique=True),
        ),
        migrations.AddField(
            model_name='finished_jobs',
            name='num_cpus',
            field=models.CharField(max_length=3, choices=[('1', '1'), ('2', '2'), ('3', '3')], default='3'),
        ),
        migrations.AddField(
            model_name='finished_jobs',
            name='num_games',
            field=models.CharField(max_length=12, default='1000'),
        ),
        migrations.AddField(
            model_name='finished_jobs',
            name='num_loops',
            field=models.CharField(max_length=5, default='10'),
        ),
        migrations.AddField(
            model_name='finished_jobs',
            name='num_players',
            field=models.CharField(max_length=2, choices=[('2', '2 Players'), ('3', '3 Players'), ('4', '4 Players'), ('5', '5 Players'), ('6', '6 Players'), ('7', '7 Players'), ('8', '8 Players')], default='2'),
        ),
        migrations.AddField(
            model_name='finished_jobs',
            name='run_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='finished_jobs',
            name='save_game_data',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='finished_jobs',
            name='sim_dir',
            field=models.CharField(max_length=200, default='C:\\Users\\Larry\\SkyDrive\\Python\\Django\\texasholdem1\\gamesim\\sim_scripts\\'),
        ),
        migrations.AddField(
            model_name='finished_jobs',
            name='status',
            field=models.CharField(max_length=10, default='pending'),
        ),
        migrations.AddField(
            model_name='finished_jobs',
            name='summary_data',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
