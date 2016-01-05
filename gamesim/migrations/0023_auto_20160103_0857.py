# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0022_analyze_job_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='grand_summary_data',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('num_players', models.CharField(max_length=2, default='2', choices=[('2', '2 Players'), ('3', '3 Players'), ('4', '4 Players'), ('5', '5 Players'), ('6', '6 Players'), ('7', '7 Players'), ('8', '8 Players')])),
                ('player_wins_total', jsonfield.fields.JSONField(null=True)),
                ('player_hands_total', jsonfield.fields.JSONField(null=True)),
                ('hand_type_wins_total', jsonfield.fields.JSONField(null=True)),
                ('hand_type_hands_total', jsonfield.fields.JSONField(null=True)),
                ('hole_hand_wins_total', jsonfield.fields.JSONField(null=True)),
                ('hole_hand_tied_wins_total', jsonfield.fields.JSONField(null=True)),
                ('hole_hand_hands_total', jsonfield.fields.JSONField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='hands',
            name='hand_type_hands_total',
        ),
        migrations.RemoveField(
            model_name='hands',
            name='hand_type_wins_total',
        ),
        migrations.RemoveField(
            model_name='hole_hands',
            name='hole_hand_hands_total',
        ),
        migrations.RemoveField(
            model_name='hole_hands',
            name='hole_hand_tied_wins_total',
        ),
        migrations.RemoveField(
            model_name='players',
            name='player_hands_total',
        ),
        migrations.RemoveField(
            model_name='players',
            name='player_wins_total',
        ),
    ]
