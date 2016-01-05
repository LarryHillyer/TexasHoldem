# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0002_auto_20151225_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hands',
            name='hand_type_hands',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='hands',
            name='hand_type_hands_total',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='hands',
            name='hand_type_wins',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='hands',
            name='hand_type_wins_total',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='hole_hands',
            name='hole_hand_hands',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='hole_hands',
            name='hole_hand_hands_total',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='hole_hands',
            name='hole_hand_tied_wins',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='hole_hands',
            name='hole_hand_tied_wins_total',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='hole_hands',
            name='hole_hand_wins',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='hole_hands',
            name='hole_hand_wins_total',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
