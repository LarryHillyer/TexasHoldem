# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:25:26 2015

@author: Larry
"""

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from gamesim.views import  index, job_queue,  job_dispatcher, \
    get_dispatcher_status, SimStatus, initialize_sim, get_loop_status, \
    reset_dispatcher, get_dispatcher_time, query_jobs, analyze, \
    Finished_Job, analyzer_dispatcher, Analyzed_Job, analyze_queue, \
    reset_dispatcher2, get_dispatcher_status2, get_dispatcher_time2, \
    get_analyze_job_status, \
    get_sim_form_data, put_sim_form_data, \
    get_pending_job_list, delete_sim_job, get_sim_job, start_dispatcher, \
    get_dispatcher_status1
    

    
urlpatterns = [
    
    url(r'^$', index.as_view(), name = 'index'),

    url(r'^job_queue/$', job_queue.as_view(), name = 'job_queue'),

    url(r'^get_sim_job/$', get_sim_job.as_view(), name = 'get_sim_job'),
    url(r'^get_sim_form_data/$', get_sim_form_data.as_view(), 
        name = 'get_sim_form_data'),
    url(r'^put_sim_form_data/$', put_sim_form_data.as_view(), 
        name = 'put_sim_form_data'),
    url(r'^get_pending_job_list/$', get_pending_job_list.as_view(), 
        name = 'get_pending_job_list'),
    url(r'^delete_sim_job/$', delete_sim_job.as_view(), 
        name = 'delete_sim_job'),
    url(r'^start_dispatcher/$', start_dispatcher.as_view(), \
        name = 'start_dispatcher'),
    url(r'^get_dispatcher_status1/$', get_dispatcher_status1.as_view(), name = \
        'get_dispatcher_status1'),
         
    url(r'^job_dispatcher/$', job_dispatcher.as_view(), \
        name = 'job_dispatcher'),
    url(r'^get_dispatcher_status/$', get_dispatcher_status.as_view(), name = \
        'get_dispatcher_status'),
    url(r'^get_loop_status/$', get_loop_status.as_view(), name = \
        'get_loop_status'),
    url(r'^reset_dispatcher/$', reset_dispatcher.as_view(), name = \
        'reset_dispatcher'),
    url(r'^get_dispatcher_time/$', get_dispatcher_time.as_view(), name = \
        'get_dispatcher_time'),
        
    url(r'^query_jobs/$', query_jobs.as_view(), name = 'query_jobs'),
    url(r'^analyze/$', analyze.as_view(), name = 'analyze'),
    url(r'^analyze_queue/$', analyze_queue.as_view(), name = 'analyze_queue'),

    url(r'^analyzer_dispatcher/$', analyzer_dispatcher.as_view(), \
        name = 'analyzer_dispatcher'),
    url(r'^get_dispatcher_status2/$', get_dispatcher_status2.as_view(), name = \
        'get_dispatcher_status2'),
    url(r'^get_dispatcher_time2/$', get_dispatcher_time2.as_view(), name = \
        'get_dispatcher_time2'),
    url(r'^get_analyze_job_status/$', get_analyze_job_status.as_view(), \
        name = 'get_analyze_job_status'),
    url(r'^reset_dispatcher2/$', reset_dispatcher2.as_view(), name = \
        'reset_dispatcher2'),


    url(r'^Finished_Job(?P<pk>[0-9]+)/$', Finished_Job.as_view(), \
        name = 'Finished_Job'),

    url(r'^analyze_queue(?P<pk>[0-9]+)/$', Analyzed_Job.as_view(), \
        name = 'analyze_queue'),


    url(r'^(?P<pk>[0-9]+)/$', SimStatus.as_view(), name = 'SimStatus'),

    url(r'^CPU1/(?P<cpu1loopdata_id>[0-9]+)/$', views.details1, \
        name = 'details1'),
    url(r'^CPU2/(?P<cpu2loopdata_id>[0-9]+)/$', views.details2, \
        name = 'details2'),
    url(r'^CPU3/(?P<cpu3loopdata_id>[0-9]+)/$', views.details3, \
        name = 'details3'),
        
    url(r'^initialize_sim/$', initialize_sim.as_view(), \
        name = 'initialize_sim'),       
]

url = format_suffix_patterns(urlpatterns)


"""
    url(r'^initial_dispatch/$', initial_dispatch.as_view(), \
        name = 'initial_dispatch'),
    url(r'^initial_dispatch2/$', initial_dispatch2.as_view(), \
        name = 'initial_dispatch2'),
"""


"""
    url(r'^create_sim/$', create_sim.as_view(), name = 'create_sim'),
    url(r'^create_job/$', views.create_job, name = 'create_job'),
    url(r'^(?P<pending_job_id>[0-9]+)/runsim/$', views.runsim, \
        name = 'runsim'),
    url(r'^(?P<running_job_id>[0-9]+)/sim_status2/$', views.sim_status2, \
        name = 'sim_status2'),
    url(r'^(?P<pending_job_id>[0-9]+)/run_sim/$', run_sim.as_view(), \
        name = 'run_sim'),


    #url(r'^(?P<pending_job_id>[0-9]+)/$',views.detail, \
        #name = 'detail'),

    #url(r'^(?P<running_job_id>[0-9]+)/sim_status/$', views.sim_status, \
        #name = 'sim_status'),

   
            
"""  

