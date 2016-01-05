# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='player_hands',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='players',
            name='player_hands_total',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='players',
            name='player_wins',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='players',
            name='player_wins_total',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='players',
            name='players_sim',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
