# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0016_dispatcher_status2_dispatcher_time2'),
    ]

    operations = [
        migrations.CreateModel(
            name='analyze_job_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('job_name', models.CharField(max_length=30)),
                ('p_pc_status', models.CharField(default='pending', max_length=10)),
                ('ht_bc_status', models.CharField(default='pending', max_length=10)),
                ('ht_pt_status', models.CharField(default='pending', max_length=10)),
                ('sp_status', models.CharField(default='pending', max_length=10)),
                ('ns_np_cp_status', models.CharField(default='pending', max_length=10)),
                ('s_np_cp_status', models.CharField(default='pending', max_length=10)),
                ('rp_bc_status', models.CharField(default='pending', max_length=10)),
                ('rp_sp_status', models.CharField(default='pending', max_length=10)),
                ('pw_p_status', models.CharField(default='pending', max_length=10)),
                ('pw_t_status', models.CharField(default='pending', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='analyze_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('job_name', models.CharField(max_length=30)),
            ],
        ),
    ]
