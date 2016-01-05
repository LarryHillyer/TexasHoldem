# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0008_auto_20151229_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu1loopdata',
            name='non_tied_hands',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='cpu1loopdata',
            name='tied_hands',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
