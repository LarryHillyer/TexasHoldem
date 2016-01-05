# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0003_auto_20151225_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulation_job',
            name='summary_data',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
