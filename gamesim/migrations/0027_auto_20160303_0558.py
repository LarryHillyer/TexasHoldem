# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0026_auto_20160302_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grand_summary_data',
            name='ht_bc',
        ),
        migrations.RemoveField(
            model_name='grand_summary_data',
            name='ht_pt',
        ),
        migrations.RemoveField(
            model_name='grand_summary_data',
            name='ns_np_cp',
        ),
        migrations.RemoveField(
            model_name='grand_summary_data',
            name='p_cp',
        ),
        migrations.RemoveField(
            model_name='grand_summary_data',
            name='p_pc',
        ),
        migrations.RemoveField(
            model_name='grand_summary_data',
            name='pw_p',
        ),
        migrations.RemoveField(
            model_name='grand_summary_data',
            name='pw_t',
        ),
        migrations.RemoveField(
            model_name='grand_summary_data',
            name='rp_bc',
        ),
        migrations.RemoveField(
            model_name='grand_summary_data',
            name='rp_sp',
        ),
        migrations.RemoveField(
            model_name='grand_summary_data',
            name='rp_t',
        ),
        migrations.RemoveField(
            model_name='grand_summary_data',
            name='s_np_cp',
        ),
        migrations.RemoveField(
            model_name='grand_summary_data',
            name='sp',
        ),
        migrations.AddField(
            model_name='analyzed_jobs',
            name='analyzed_job_data',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='grand_summary_data',
            name='analyzed_gs_data',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
