# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0021_delete_analyze_job_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='analyze_job_status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('job_name', models.CharField(max_length=30)),
                ('p_pc_status', models.CharField(default='pending', max_length=10)),
                ('ht_bc_status', models.CharField(default='pending', max_length=10)),
                ('ht_pt_status', models.CharField(default='pending', max_length=10)),
                ('rp_t_status', models.CharField(default='pending', max_length=10)),
                ('sp_status', models.CharField(default='pending', max_length=10)),
                ('ns_np_cp_status', models.CharField(default='pending', max_length=10)),
                ('s_np_cp_status', models.CharField(default='pending', max_length=10)),
                ('p_cp_status', models.CharField(default='pending', max_length=10)),
                ('rp_bc_status', models.CharField(default='pending', max_length=10)),
                ('rp_sp_status', models.CharField(default='pending', max_length=10)),
                ('pw_p_status', models.CharField(default='pending', max_length=10)),
                ('pw_t_status', models.CharField(default='pending', max_length=10)),
            ],
        ),
    ]
