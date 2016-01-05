# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0014_auto_20151229_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='analyzed_jobs',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('job_name', models.CharField(null=True, unique=True, max_length=30)),
                ('sim_job_names', jsonfield.fields.JSONField(null=True)),
                ('status', models.CharField(default='pending', max_length=10)),
                ('run_time', models.DateTimeField(null=True)),
                ('finish_time', models.DateTimeField(null=True)),
                ('num_players', models.CharField(default='2', max_length=2)),
                ('sim_dir', models.CharField(default='C:\\Users\\Larry\\SkyDrive\\Python\\Django\\texasholdem1\\gamesim\\sim_scripts\\', max_length=200)),
                ('summary_data', jsonfield.fields.JSONField(null=True)),
                ('analyzed_files', jsonfield.fields.JSONField(null=True)),
            ],
            options={
                'ordering': ('run_time',),
            },
        ),
    ]
