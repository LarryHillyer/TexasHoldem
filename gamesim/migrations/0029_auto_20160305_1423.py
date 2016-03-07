# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0028_auto_20160303_0559'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyzed_jobs',
            name='grand_num_games',
            field=models.CharField(null=True, max_length=20),
        ),
        migrations.AddField(
            model_name='analyzed_jobs',
            name='num_games',
            field=models.CharField(null=True, max_length=20),
        ),
    ]
