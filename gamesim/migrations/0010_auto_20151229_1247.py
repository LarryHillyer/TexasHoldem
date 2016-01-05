# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0009_auto_20151229_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu2loopdata',
            name='non_tied_hands',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='cpu2loopdata',
            name='tied_hands',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
