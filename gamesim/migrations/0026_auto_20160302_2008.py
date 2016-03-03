# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0025_auto_20160302_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyzed_jobs',
            name='ht_bc',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='analyzed_jobs',
            name='ht_pt',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='analyzed_jobs',
            name='ns_np_cp',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='analyzed_jobs',
            name='p_cp',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='analyzed_jobs',
            name='p_pc',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='analyzed_jobs',
            name='pw_p',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='analyzed_jobs',
            name='pw_t',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='analyzed_jobs',
            name='rp_bc',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='analyzed_jobs',
            name='rp_sp',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='analyzed_jobs',
            name='rp_t',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='analyzed_jobs',
            name='s_np_cp',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='analyzed_jobs',
            name='sp',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='grand_summary_data',
            name='ht_bc',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='grand_summary_data',
            name='ht_pt',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='grand_summary_data',
            name='ns_np_cp',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='grand_summary_data',
            name='p_cp',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='grand_summary_data',
            name='p_pc',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='grand_summary_data',
            name='pw_p',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='grand_summary_data',
            name='pw_t',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='grand_summary_data',
            name='rp_bc',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='grand_summary_data',
            name='rp_sp',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='grand_summary_data',
            name='rp_t',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='grand_summary_data',
            name='s_np_cp',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='grand_summary_data',
            name='sp',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
