# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:45:45 2015

@author: Larry
"""

from rest_framework import serializers
from gamesim.models import Simulation_Job, dispatcher_status, loop_status, \
    dispatcher_time, finished_jobs, analyze_job_status, dispatcher_status2, \
    dispatcher_time2, analyzed_jobs

class Simulation_Job_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Simulation_Job
        fields = ['id', 'job_name','status','run_time','finish_time', \
        'num_players', 'num_cpus', 'num_loops', 'num_games', 'sim_dir', \
        'save_game_data']
        
class dispatcher_status_serializer(serializers.ModelSerializer):
    class Meta:
        model = dispatcher_status
        fields = ['id', 'status', 'job_name',]
        
class loop_status_serializer(serializers.ModelSerializer):
    class Meta:
        model = loop_status
        fields = ['id', 'job_name', 'loop_num', 'loop_time', \
            'cpu1_exit_status', 'cpu2_exit_status', 'cpu3_exit_status',]
            
class dispatcher_time_serializer(serializers.ModelSerializer):
    class Meta:
        model = dispatcher_time
        fields = ['time_delta']
"""        
class finished_job_list_serializer(serializers.ModelSerializer):
    class Meta:
        model = finished_jobs
        fields = ['finished_job_list']
"""        
class finished_jobs_serializer(serializers.ModelSerializer):
    class Meta:
        model = finished_jobs
        fields = ['id', 'job_name','status','run_time','finish_time', \
            'num_players', 'num_cpus', 'num_loops', 'num_games', 'sim_dir',\
            'summary_data', 'save_game_data']

        
class analyzed_jobs_serializer(serializers.ModelSerializer):
    class Meta:
        model = analyzed_jobs
        fields = ['id', 'job_name','sim_job_names','status','run_time', \
        'finish_time', 'num_players', 'sim_dir','summary_data', \
        'analyzed_files']
        
class analyzed_jobs2_serializer(serializers.ModelSerializer):
    class Meta:
        model = analyzed_jobs
        fields = ['job_name','analyzed_job_data']
       
class analyze_job_status_serializer(serializers.ModelSerializer):
    class Meta:
        model = analyze_job_status
        fields = ['id', 'job_name','p_pc_status','ht_bc_status', 'ht_pt_status', \
            'sp_status', 'rp_t_status','s_np_cp_status','ns_np_cp_status', \
            'p_cp_status', 'rp_bc_status', 'rp_sp_status', 'pw_p_status', \
            'pw_t_status']
        
class dispatcher_status2_serializer(serializers.ModelSerializer):
    class Meta:
        model = dispatcher_status2
        fields = ['id', 'status', 'job_name',]
class dispatcher_time2_serializer(serializers.ModelSerializer):
    class Meta:
        model = dispatcher_time2
        fields = ['time_delta']
