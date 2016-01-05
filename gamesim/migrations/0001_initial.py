# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cards',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('card_suits', jsonfield.fields.JSONField(default=dict)),
                ('card_ranks', jsonfield.fields.JSONField(default=dict)),
                ('card_rank_numbers', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='cpu1loopdata',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('run_time', models.DateTimeField()),
                ('num_players', models.IntegerField()),
                ('cpu_num', models.CharField(max_length=3)),
                ('non_tied_hands', jsonfield.fields.JSONField(verbose_name='finished non tied hand', default=dict)),
                ('tied_hands', jsonfield.fields.JSONField(verbose_name='finished tied hand', default=dict)),
                ('parent_data', jsonfield.fields.JSONField(verbose_name='loop summary data returned to parent', default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='cpu2loopdata',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('run_time', models.DateTimeField()),
                ('num_players', models.IntegerField()),
                ('cpu_num', models.CharField(max_length=3)),
                ('non_tied_hands', jsonfield.fields.JSONField(verbose_name='finished non tied hand', default=dict)),
                ('tied_hands', jsonfield.fields.JSONField(verbose_name='finished tied hand', default=dict)),
                ('parent_data', jsonfield.fields.JSONField(verbose_name='loop summary data returned to parent', default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='cpu3loopdata',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('run_time', models.DateTimeField()),
                ('num_players', models.IntegerField()),
                ('cpu_num', models.CharField(max_length=3)),
                ('non_tied_hands', jsonfield.fields.JSONField(verbose_name='finished non tied hand', default=dict)),
                ('tied_hands', jsonfield.fields.JSONField(verbose_name='finished tied hand', default=dict)),
                ('parent_data', jsonfield.fields.JSONField(verbose_name='loop summary data returned to parent', default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='dispatcher_status',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('status', models.CharField(max_length=8, choices=[('Stopped', 'Stopped'), ('Idle', 'Idle'), ('Running', 'Running'), ('Finished', 'Finished')], default='Stopped')),
                ('job_name', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='hands',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('hand_types', jsonfield.fields.JSONField(default=dict)),
                ('hand_type_ranks', jsonfield.fields.JSONField(default=dict)),
                ('hand_type_wins', jsonfield.fields.JSONField(default=dict)),
                ('hand_type_hands', jsonfield.fields.JSONField(default=dict)),
                ('hand_type_wins_total', jsonfield.fields.JSONField(default=dict)),
                ('hand_type_hands_total', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='hole_hands',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('permutations', jsonfield.fields.JSONField(default=dict)),
                ('hole_hand_wins', jsonfield.fields.JSONField(default=dict)),
                ('hole_hand_tied_wins', jsonfield.fields.JSONField(default=dict)),
                ('hole_hand_hands', jsonfield.fields.JSONField(default=dict)),
                ('hole_hand_wins_total', jsonfield.fields.JSONField(default=dict)),
                ('hole_hand_tied_wins_total', jsonfield.fields.JSONField(default=dict)),
                ('hole_hand_hands_total', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='loop_status',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('job_name', models.CharField(max_length=30)),
                ('loop_num', models.CharField(max_length=4)),
                ('loop_time', models.CharField(max_length=30)),
                ('cpu1_exit_status', models.CharField(max_length=3)),
                ('cpu2_exit_status', models.CharField(max_length=3)),
                ('cpu3_exit_status', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='players',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('players_initial', jsonfield.fields.JSONField(default=dict)),
                ('player_wins_initial', jsonfield.fields.JSONField(default=dict)),
                ('player_hands_initial', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='python_scripts',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('python', models.CharField(max_length=25)),
                ('parent_process', models.CharField(max_length=30)),
                ('child_process', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Simulation_Job',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('job_name', models.CharField(unique=True, max_length=30, null=True)),
                ('status', models.CharField(max_length=10, default='pending')),
                ('run_time', models.DateTimeField(auto_now_add=True)),
                ('finish_time', models.DateTimeField(null=True)),
                ('num_players', models.CharField(max_length=2, choices=[('2', '2 Players'), ('3', '3 Players'), ('4', '4 Players'), ('5', '5 Players'), ('6', '6 Players'), ('7', '7 Players'), ('8', '8 Players')], default='2')),
                ('num_cpus', models.CharField(max_length=3, choices=[('1', '1'), ('2', '2'), ('3', '3')], default='3')),
                ('num_loops', models.CharField(max_length=5, default='10')),
                ('num_games', models.CharField(max_length=12, default='1000')),
                ('sim_dir', models.CharField(max_length=200, default='C:\\Users\\Larry\\SkyDrive\\Python\\Django\\texasholdem1\\gamesim\\sim_scripts\\')),
            ],
            options={
                'ordering': ('run_time',),
            },
        ),
        migrations.AddField(
            model_name='cpu3loopdata',
            name='simulation_job',
            field=models.ForeignKey(to='gamesim.Simulation_Job'),
        ),
        migrations.AddField(
            model_name='cpu2loopdata',
            name='simulation_job',
            field=models.ForeignKey(to='gamesim.Simulation_Job'),
        ),
        migrations.AddField(
            model_name='cpu1loopdata',
            name='simulation_job',
            field=models.ForeignKey(to='gamesim.Simulation_Job'),
        ),
    ]
