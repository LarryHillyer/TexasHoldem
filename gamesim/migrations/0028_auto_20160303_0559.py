# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0027_auto_20160303_0558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analyzed_jobs',
            name='ht_bc',
        ),
        migrations.RemoveField(
            model_name='analyzed_jobs',
            name='ht_pt',
        ),
        migrations.RemoveField(
            model_name='analyzed_jobs',
            name='ns_np_cp',
        ),
        migrations.RemoveField(
            model_name='analyzed_jobs',
            name='p_cp',
        ),
        migrations.RemoveField(
            model_name='analyzed_jobs',
            name='p_pc',
        ),
        migrations.RemoveField(
            model_name='analyzed_jobs',
            name='pw_p',
        ),
        migrations.RemoveField(
            model_name='analyzed_jobs',
            name='pw_t',
        ),
        migrations.RemoveField(
            model_name='analyzed_jobs',
            name='rp_bc',
        ),
        migrations.RemoveField(
            model_name='analyzed_jobs',
            name='rp_sp',
        ),
        migrations.RemoveField(
            model_name='analyzed_jobs',
            name='rp_t',
        ),
        migrations.RemoveField(
            model_name='analyzed_jobs',
            name='s_np_cp',
        ),
        migrations.RemoveField(
            model_name='analyzed_jobs',
            name='sp',
        ),
    ]
