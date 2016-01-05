2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:58:52 2015

@author: Larry
"""

import numpy as np
import subprocess
import json
import time
import os
import sys
import mysql.connector
import datetime as dt
import pytz
import TexasHoldemInitialize2 as th_i


def delete_loop_status_data():
    
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])    
        cur = cnx.cursor()
        
        delete_loop_status = ("delete from gamesim_loop_status;")
        cur.execute(delete_loop_status)

        cnx.commit()
        cnx.close()
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
    return

def get_run_time(id1):
    
    run_time = dt.datetime.now(pytz.utc)
    
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])    
        cur = cnx.cursor()    
        update_run_time = ("update gamesim_simulation_job set run_time = "
                        "%(run_time)s where id = %(id)s; ")
                        
        insert_data = {'run_time': run_time, 'id': id1}
    
        cur.execute(update_run_time, insert_data)        
        cnx.commit()        
        cnx.close()
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
        
    return run_time


def runProc(proc_num):
    proc = subprocess.Popen([python, childProcess + proc_num +'.py', \
        str(sim_id)], stdout = subprocess.PIPE)
    return proc
    
def spawnChildren():
    procs = []
    for i in range(num_cpus):
        proc = runProc(str(i+1))
        procs.append(proc)
    
    return procs
    
def getExitStatus():
    
    print('Loop Number:  ', loop_num)
    
    end2 = time.time()
    loop_time = end2 - start2
    print('Finished Inner Loop in % 25.3f seconds' % (loop_time))
    job_name = 'sim' + str(sim_id)
   
    for proc in procs:
        out, err = proc.communicate()
      
    if num_cpus == 1:
        while procs[0].poll() is None:
                time.sleep(1)
                
        print('Exit Status 1', procs[0].poll())
        
    elif num_cpus == 2:
        while procs[0].poll() is None and procs[1].poll() is None:
                time.sleep(1)
                
        print('Exit Status 1', procs[0].poll())
        print('Exit Status 2', procs[1].poll())
                
    elif num_cpus == 3:
        while procs[0].poll() is None and procs[1].poll() is None and \
            procs[2].poll() is None:
                time.sleep(1)
        
        try:
            cnx = mysql.connector.connect(user=db_params['username'], \
            password = db_params['password'], database= db_params['database'])           
            cur = cnx.cursor()
            
            insert_loop_status =("insert into gamesim_loop_status "
                "(job_name, loop_num, loop_time, cpu1_exit_status, " 
                "cpu2_exit_status, cpu3_exit_status) "
                "values (%(job_name)s, %(loop_num)s, %(loop_time)s, "
                "%(cpu1_exit_status)s, %(cpu2_exit_status)s, "
                "%(cpu3_exit_status)s); ")
                            
            loop_status_data ={'job_name': job_name, \
                'loop_num': str(loop_num), \
                'loop_time': str(loop_time), \
                'cpu1_exit_status': str(procs[0].poll()), \
                'cpu2_exit_status': str(procs[1].poll()), \
                'cpu3_exit_status': str(procs[2].poll()), }
                
                
            cur.execute(insert_loop_status, loop_status_data)
            
            cnx.commit()
            cnx.close()
                
        except mysql.connector.Error as e:
            print(e.args[0])
            print(e.args[1])
            cnx.close()
            
        print('Exit Status 1', procs[0].poll())
        print('Exit Status 2', procs[1].poll())
        print('Exit Status 3', procs[2].poll())
        
    return
    
    
def combineTotals(total_number_of_games2):
    
    for i, list1 in enumerate(parent_data):
        total_number_of_games2 = total_number_of_games2 + list1['total_games']   
        for holeHand in permutations:
            hole_hand_wins_total[holeHand] = \
                hole_hand_wins_total[holeHand] + \
                list1['hole_hand_wins'][holeHand]
            hole_hand_tied_wins_total[holeHand] = \
                hole_hand_tied_wins_total[holeHand] + \
                list1['hole_hand_tied_wins'][holeHand]
            hole_hand_hands_total[holeHand] = \
                hole_hand_hands_total[holeHand] + \
                list1['hole_hand_hands'][holeHand]
        for player in list1['player_wins'].keys():
            player_wins_total[player] = player_wins_total[player] + \
                list1['player_wins'][player]
            player_hands_total[player] = player_hands_total[player] + \
                list1['player_hands'][player]
        for handType in list1['hand_type_wins'].keys():
            hand_type_wins_total[handType] = hand_type_wins_total[handType] + \
                list1['hand_type_wins'][handType]
            hand_type_hands_total[handType] = hand_type_hands_total[handType] + \
                list1['hand_type_hands'][handType]    
    return total_number_of_games2
    
def putPlayerProbs(total_number_of_games2):
    for player in player_wins.keys():
        player_probs[player] = player_wins_total[player]/total_number_of_games2  
    return
    
def putHandTypeProbs(total_number_of_games2):
    for handType in hand_type_wins.keys():
        hand_type_probs[handType] = hand_type_wins_total[handType]/total_number_of_games2
    
        if hand_type_hands_total[handType] > 0:
            hand_type_probs2[handType] = hand_type_wins_total[handType] / \
            hand_type_hands_total[handType]
        else:
            hand_type_probs2[handType] = 0
    return
    
def putHoleHandProbs(total_number_of_games2):
    for holeHand in permutations:
        hole_hand_probs[holeHand] = \
            (hole_hand_wins_total[holeHand] \
            + hole_hand_tied_wins_total[holeHand])/ total_number_of_games2
    
        if hole_hand_hands_total[holeHand] > 0:    
            hole_hand_probs2[holeHand] = \
                (hole_hand_wins_total[holeHand] + \
                hole_hand_tied_wins_total[holeHand]) / \
                hole_hand_hands_total[holeHand]
        else:
            hole_hand_probs2[holeHand] = 0        
    
        if len(holeHand) == 2:
            hole_hand_norm_probs[holeHand] = \
            hole_hand_probs[holeHand]/6
        elif holeHand[2:] == 'S':
            hole_hand_norm_probs[holeHand] = \
            hole_hand_probs[holeHand]/4
        elif holeHand[2:] == 'NS':
            hole_hand_norm_probs[holeHand] = \
            hole_hand_probs[holeHand]/12 
    return
    
def getMinNormProb():
    min_norm_prob_value = np.min(list(hole_hand_norm_probs.values()))
    for name, value in hole_hand_norm_probs.items():
        if value == min_norm_prob_value:
            min_norm_prob_key = name
            break
    return min_norm_prob_key
    
def putHoleHandRelProbs():
    for holeHand in permutations:
        minKey = getMinNormProb()
        if hole_hand_norm_probs[minKey] > 0:    
            hole_hand_rel_probs[holeHand] = \
                hole_hand_norm_probs[holeHand] / \
                hole_hand_norm_probs[minKey]
        else:
            hole_hand_rel_probs[holeHand] = 0        

        if hole_hand_probs2[minKey] > 0:    
            hole_hand_rel_probs2[holeHand] = \
                hole_hand_probs2[holeHand] / \
                hole_hand_probs2[minKey]    
        else:
            hole_hand_rel_probs2[holeHand] = 0           
    return
    
def sumProbs():
    sum_of_hand_type_probs = np.sum(list(hand_type_probs.values()))           
    sum_of_player_probs = np.sum(list(player_probs.values()))
    sum_of_hole_hand_probs = np.sum(list(hole_hand_probs.values())) 
    return sum_of_hand_type_probs, sum_of_player_probs, sum_of_hole_hand_probs
    

def putSummaryData(num_Players,num_Games):
    
    summary_data = {}
    summary_data['players'] = players    
    summary_data['card_suits'] = card_suits    
    summary_data['card_ranks'] = card_ranks    
    summary_data['card_rank_numbers'] = card_rank_numbers    
    summary_data['hand_types'] = hand_types
    summary_data['hand_type_ranks'] = hand_type_ranks    
    summary_data['permutations'] = permutations        
    summary_data['total_number_of_games2'] = total_number_of_games2    
    summary_data['player_wins_total'] = player_wins_total
    summary_data['player_hands_total'] = player_hands_total
    summary_data['player_probs'] = player_probs
    summary_data['hand_type_wins_total'] = hand_type_wins_total
    summary_data['hand_type_hands_total'] = hand_type_hands_total
    summary_data['hand_type_probs'] = hand_type_probs
    summary_data['hand_type_probs2'] = hand_type_probs2
    summary_data['hole_hand_wins_total'] = hole_hand_wins_total
    summary_data['hole_hand_tied_wins_total'] = hole_hand_tied_wins_total
    summary_data['hole_hand_hands_total'] = hole_hand_hands_total
    summary_data['hole_hand_probs'] = hole_hand_probs
    summary_data['hole_hand_probs2'] = hole_hand_probs2
    summary_data['hole_hand_norm_probs'] = hole_hand_norm_probs
    summary_data['hole_hand_rel_probs'] = hole_hand_rel_probs
    summary_data['hole_hand_rel_probs2'] = hole_hand_rel_probs2
    
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])            
        cur = cnx.cursor()
    
        update_sim_job = ("update gamesim_simulation_job set summary_data = "
                    "%(summary_data)s where id = %(id)s;")
                    
        update_data = {'summary_data': json.dumps(summary_data), \
            'id': str(sim_id)}
        cur.execute(update_sim_job, update_data)       
        cnx.commit()
        cnx.close()
    
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
               
    return
    
def getCpuLoopData(rows, cpuLoopData):
    for row in rows: 
        cpuLoopData = getLoopData(row,cpuLoopData)                
    for loop in cpuLoopData:
        putParentData(loop)             
    return
    
def getLoopData(row, cpuLoopData):
    
    cpuLoopData_1 = {}
    cpuLoopData_1['run_time'] = row[0]                            
    cpuLoopData_1['num_players'] = row[1]
    cpuLoopData_1['parent_data'] = json.loads(row[2])
    cpuLoopData.append(cpuLoopData_1)
    
    return cpuLoopData
    
def putParentData(loop):
    loop_dict = {}
    for key, values in loop['parent_data'].items():
        loop_dict[key] = values
    loop_dict['run_time'] = loop['run_time']
    loop_dict['num_players'] = loop['num_players']
    parent_data.append(loop_dict)
    
    return parent_data
   
def getParentData2():
    
    try:
        cpu1LoopData, cpu2LoopData, cpu3LoopData = [], [], []
        
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])    
        
        cur = cnx.cursor()
    
        select_cpu1LoopData = ("select run_Time, num_players, parent_data "
            "from gamesim_cpu1LoopData where num_players = %(num_players)s and "
            "run_time = %(run_time)s;")
        select_cpu2LoopData = ("select run_time, num_players, parent_data "
            "from gamesim_cpu2LoopData where num_players = %(num_players)s and "
            "run_time = %(run_time)s;")
        select_cpu3LoopData = ("select run_time, num_players, parent_data "
            "from gamesim_cpu3LoopData where num_players = %(num_players)s and "
            "run_time = %(run_time)s;")
            
        query_data = {'num_players': num_players, "run_time": run_time}
        
        cur.execute(select_cpu1LoopData, query_data)
        rows = cur.fetchall()
        getCpuLoopData(rows, cpu1LoopData)
                                    
        cur.execute(select_cpu2LoopData, query_data)
        rows = cur.fetchall()
        getCpuLoopData(rows, cpu2LoopData)
                            
        cur.execute(select_cpu3LoopData, query_data)
        rows = cur.fetchall()
        getCpuLoopData(rows, cpu3LoopData)
                
        cnx.close()
        
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
    return
    
def put_finish_time():
    
    try:    
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])    
        cur = cnx.cursor()
    
        update_simulation_job = ("update gamesim_simulation_job "
                            "set finish_time = %(finish_time)s, "
                            "status = %(status)s "
                            "where run_time = %(run_time)s;")
                                
        update_data = {'finish_time': finish_time, 'run_time': run_time, \
            'status': 'finished'}
    
        cur.execute(update_simulation_job, update_data)
        
        cnx.commit() 
        cnx.close()
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
    return
    
###############################################################################
##########    Start  GameSimulation   #########################################
###############################################################################
    
db_params = {'username':'texasholdem', 'password': 'Texasholdem123', \
    'database': 'texasholdem_db'}

th_i.set_global_sql_variables()
    
delete_loop_status_data()
    
sim_id = int(sys.argv[1])

num_players, num_cpus, num_loops, num_games, sim_dir = \
    th_i.getSimulationParameters(sim_id)

os.chdir(sim_dir)

start1 = time.time()
run_time = get_run_time(sim_id)

python, childProcess = th_i.get_python_scripts()
players, player_wins_total, player_hands_total = th_i.get_initial_players()
card_suits, card_ranks, card_rank_numbers = th_i.get_cards()
hand_types, hand_type_ranks = th_i.get_hands()
permutations = th_i.get_hole_hands()

player_wins_grand_total, player_hands_grand_total = \
    th_i.get_players_grand_total()
    
hand_type_wins_grand_total, hand_type_hands_grand_total = \
    th_i.get_hand_type_grand_total()
    
hole_hand_wins_grand_total, hole_hand_hands_grand_total, \
    hole_hand_tied_wins_grand_total = th_i.get_hole_hand_grand_total()
    
player_wins_total, player_hands_total, hand_type_wins_total, hand_type_hands_total, \
    hole_hand_wins_total, hole_hand_hands_total, \
    hole_hand_tied_wins_total, = th_i.getInitialCounters()

player_probs, hand_type_probs, hand_type_probs2, hole_hand_probs, \
    hole_hand_probs2, hole_hand_norm_probs, \
    hole_hand_rel_probs, hole_hand_rel_probs2 = \
    th_i.getInitialProbLists()
    
total_number_of_games2 = 0

players, player_wins_total, player_hands_total = th_i.putPlayers(num_players,players,\
    player_wins_total, player_hands_total)
        
for loop_num in range(num_loops):

    number_of_games = num_games
    
    player_wins, player_hands, hand_type_wins, hand_type_hands,\
        hole_hand_wins, hole_hand_hands,\
        hole_hand_tied_wins = th_i.getInitialCounters()
        
    player_wins, player_hands = th_i.getPlayerCounters()
    
    start2 = time.time()
    procs = spawnChildren()
    getExitStatus()
         
###############################################################################
"""
Calculating Statistical Probablities Based Upon Simulation
"""
###############################################################################
parent_data = []
getParentData2()

total_number_of_games2 = combineTotals(total_number_of_games2)

putPlayerProbs(total_number_of_games2)
putHandTypeProbs(total_number_of_games2)
putHoleHandProbs(total_number_of_games2)
putHoleHandRelProbs()
        
sum_of_hand_type_probs, sum_of_player_probs, sum_of_hole_hand_probs \
    = sumProbs()

putSummaryData(str(num_players), str(num_cpus*num_loops*\
    num_games))


end1 = time.time()
print('Finished Simulation in % 25.3f seconds' % (end1 - start1))

finish_time = dt.datetime.now(pytz.utc)
put_finish_time()    


