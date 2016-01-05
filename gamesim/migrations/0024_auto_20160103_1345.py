# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0023_auto_20160103_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='player_hands_total',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='players',
            name='player_wins_total',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
