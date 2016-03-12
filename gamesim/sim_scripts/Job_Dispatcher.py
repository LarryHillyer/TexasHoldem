# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:12:40 2015

@author: Larry
"""

import mysql.connector
import subprocess
import time
import sys

def get_pending_jobs():
    
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])    
        cur = cnx.cursor()
    
        select_pending_jobs = ("select * from gamesim_simulation_job "
                        "where status = 'pending'; ")
    
        cur.execute(select_pending_jobs)
        
        pending_jobs1 = cur.fetchall()

        for job in pending_jobs1:
            
          pending_jobs2 = {}
          pending_jobs2['simulation_job_id'] = job[0]
          pending_jobs2['job_name'] = job[1]
          pending_jobs2['status'] = job[2]          
          pending_jobs2['run_time'] = job[3]
          pending_jobs2['finish_time'] = job[4]
          pending_jobs2['num_players'] = job[5]
          pending_jobs2['num_cpus'] = job[6]
          pending_jobs2['num_loops'] = job[7]
          pending_jobs2['num_games'] = job[8]
          pending_jobs2['sim_dir'] = job[9]
          pending_jobs.append(pending_jobs2)
        
        cnx.close()
        
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
    
    return
    
def update_status(run_status):
    
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])    
        cur = cnx.cursor()
    
        update_status = (" update gamesim_simulation_job "
                        " set status = 'running' "
                        "where run_time = %(run_status)s; ")
                        
        update_data = {'run_status': run_status}
    
        cur.execute(update_status, update_data)
        
        cnx.commit()
        cnx.close()
    
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])

    return
    
def get_dispatch_status():
    cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])    
    cur = cnx.cursor()
    
    select_dispatch_status = ("select status from gamesim_dispatcher_status "
                    "where id = 1;")
    
    cur.execute(select_dispatch_status)
    
    dispatch_status = cur.fetchone()
    return dispatch_status    
    
    
    
        
def get_running_job(sim_id):
    
    try:
        dispatch_status = get_dispatch_status()
        
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])    
        cur = cnx.cursor()
    
        select_running_job = ("select * from gamesim_simulation_job "
                        "where id = %(sim_id)s and status = 'running'; ")
    
        select_data = {'sim_id': sim_id }
        cur.execute(select_running_job, select_data)
        
        running_job = cur.fetchone()
        
        cur = cnx.cursor()
        
        update_status = ("update gamesim_dispatcher_status "
                        "set status = %(status)s, "
                        "job_name = %(job_name)s  "
                        "where id = %(id)s;")
        
        if running_job == () or running_job is None or dispatch_status == \
            'Reset':
            job_running = False
            job_name = 'sim' + str(sim_id)
            update_data = {'id': 1, 'job_name':job_name, 'status':'loading'}
            
        else:
            job_running = True
            job_name = running_job[1]
            update_data = {'id': 1, 'job_name':job_name, 'status':'Running'}
                        
    
        cur.execute(update_status, update_data)           
        cnx.commit()
        cnx.close()

        
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
    
    
    return job_running
         
###############################################################################
#############  Start Main Program                     #########################         
###############################################################################
         
db_params = {'username':'texasholdem1', 'password':'Texasholdem123', \
    'database':'texasholdem_db'}
    
sim_script = 'Parent_Texas_Holdem_Play.py'

sim_id = int(sys.argv[1])
    
try:    
    cnx = mysql.connector.connect(user=db_params['username'], password = \
        db_params['password'], database= db_params['database'])    
        
    cur = cnx.cursor()
    
    update_dispatcher_status = ("update gamesim_dispatcher_status "
        "set status = %(status)s "
        "where id = %(id)s;")
                                
    update_data = {'id': 1 ,'status': 'Running'}
    
    cur.execute(update_dispatcher_status, update_data)
        
    cnx.commit() 
    cnx.close()
except:
    pass


pending_jobs = []
get_pending_jobs()

running_job = ()
job_running = get_running_job(sim_id)

while pending_jobs != []:
    
    next_job = pending_jobs[0]
    min_run_time_job = (0,pending_jobs[0]['run_time'])
    for i, job in enumerate(pending_jobs, 1):
        if job['run_time'] < min_run_time_job[1]:
            min_run_time_job = (i,job['run_time'])
            next_job = job[i]
            
    update_status(next_job['run_time'])
    
    
    args = ['python', next_job['sim_dir'] + sim_script, \
        str(next_job['simulation_job_id'])]
        
    subprocess.Popen(args, stdout = subprocess.PIPE)
    
    job_running = get_running_job(next_job['simulation_job_id'])
    print("job_dispatcher script")
    while job_running == True:
        job_running = get_running_job(next_job['simulation_job_id'])
        if job_running == False:
            break
        time.sleep(5)
        
    pending_jobs = []
    get_pending_jobs()
    time.sleep(5)
    
try:    
    cnx = mysql.connector.connect(user=db_params['username'], password = \
        db_params['password'], database= db_params['database'])    
        
    cur = cnx.cursor()
    
    update_dispatcher_status = ("update gamesim_dispatcher_status "
        "set status = %(status)s, "
        "job_name = %(job_name)s "
        "where id = %(id)s;")
                                
    update_data = {'id': 1 ,'status': 'Finished', 'job_name':''}
    
    cur.execute(update_dispatcher_status, update_data)
        
    cnx.commit() 
    cnx.close()
except:
    pass        
    