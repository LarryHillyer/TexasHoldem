# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:00:05 2015

@author: Larry
"""
import json
import numpy as np
import sys
import os
#import time
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "texasholdem1.settings")

import mysql.connector
import pytz
import datetime as dt

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from mpl_toolkits.mplot3d import axes3d 
from matplotlib import cm
import mpld3
from mpld3 import plugins

def set_global_sql_variables():
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])    
        cur = cnx.cursor()
        
        set_global_variables = ("set global max_allowed_packet=419430000; "
                                "set global key_buffer_size=268435456; "
                                "set global table_open_cache=256; "
                                "set global sort_buffer_size=4194304; "
                                "set global read_buffer_size=1048576;")

        cur.execute(set_global_variables, multi = True)
        
        cnx.commit()
        cnx.close()

        
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
        
def create_analyze_job_status(job_name):
    
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])    
        cur = cnx.cursor()
        
        delete_loop_status = ("delete from gamesim_analyze_job_status;")
        cur.execute(delete_loop_status)
        cnx.commit()
        
        insert_analyze_job_status = ("insert into gamesim_analyze_job_status "
            "(job_name) values (%(job_name)s);")
        insert_data = {'job_name': job_name}
        
        cur.execute(insert_analyze_job_status, insert_data)

        cnx.commit()
        cnx.close()
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
    return
    
    
    return 
        
def get_run_time(id1):
    
    run_time = dt.datetime.now(pytz.utc)
    
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])    
        cur = cnx.cursor()    
        update_run_time = ("update gamesim_analyzed_jobs set run_time = "
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
        
def getSummaryData(job_name):
    
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])      
        cur = cnx.cursor()
    
        select_sim_job = ("select summary_data from gamesim_analyzed_jobs "
                        "where job_name = %(job_name)s;")
                        
        select_data = {'job_name': job_name}
    
        cur.execute(select_sim_job, select_data)
        summary_data1 = cur.fetchone()
        summary_data = json.loads(summary_data1[0])

    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
    
    players = summary_data['players']
    card_suits = summary_data['card_suits']
    card_ranks = summary_data['card_ranks']
    card_rank_numbers = summary_data['card_rank_numbers']
    hand_types = summary_data['hand_types']
    hand_type_ranks = summary_data['hand_type_ranks']
    permutations = summary_data['permutations']
    
    total_number_of_games2 = summary_data['total_number_of_games2']
    player_wins_total = summary_data['player_wins_total']
    #player_hands_total = summary_data['player_hands_total']  
    player_probs = summary_data['player_probs']
    hand_type_wins_total = summary_data['hand_type_wins_total']
    hand_type_hands_total = summary_data['hand_type_hands_total']
    hand_type_probs = summary_data['hand_type_probs']
    hand_type_probs2 = summary_data['hand_type_probs2']
    hole_hand_wins_total = summary_data['hole_hand_wins_total']
    hole_hand_tied_wins_total = summary_data['hole_hand_tied_wins_total']
    hole_hand_hands_total = summary_data['hole_hand_hands_total']
    hole_hand_probs = summary_data['hole_hand_probs']
    hole_hand_probs2 = summary_data['hole_hand_probs2']
    hole_hand_norm_probs = summary_data['hole_hand_norm_probs']
    hole_hand_rel_probs = summary_data['hole_hand_rel_probs']
    hole_hand_rel_probs2 = summary_data['hole_hand_rel_probs2']
    
    grand_total_number_of_games = summary_data['grand_total_number_of_games']
    player_wins_grand_total = summary_data['player_wins_grand_total']
    #player_hands_total = summary_data['player_hands_total']  
    player_grand_probs = summary_data['player_grand_probs']
    hand_type_wins_grand_total = summary_data['hand_type_wins_grand_total']
    hand_type_hands_grand_total = summary_data['hand_type_hands_grand_total']
    hand_type_grand_probs = summary_data['hand_type_grand_probs']
    hand_type_grand_probs2 = summary_data['hand_type_grand_probs2']
    hole_hand_wins_grand_total = summary_data['hole_hand_wins_grand_total']
    hole_hand_tied_wins_grand_total = summary_data['hole_hand_tied_wins_grand_total']
    hole_hand_hands_grand_total = summary_data['hole_hand_hands_grand_total']
    hole_hand_grand_probs = summary_data['hole_hand_grand_probs']
    hole_hand_grand_probs2 = summary_data['hole_hand_grand_probs2']
    hole_hand_norm_grand_probs = summary_data['hole_hand_norm_grand_probs']
    hole_hand_rel_grand_probs = summary_data['hole_hand_rel_grand_probs']
    hole_hand_rel_grand_probs2 = summary_data['hole_hand_rel_grand_probs2']
        
    return players, card_suits, card_ranks, card_rank_numbers, hand_types, \
        hand_type_ranks, permutations, total_number_of_games2, \
        player_wins_total, player_probs, hand_type_wins_total, \
        hand_type_hands_total, hand_type_probs, hand_type_probs2, \
        hole_hand_wins_total, hole_hand_tied_wins_total, \
        hole_hand_hands_total, hole_hand_probs, hole_hand_probs2, \
        hole_hand_norm_probs, hole_hand_rel_probs, hole_hand_rel_probs2, \
        grand_total_number_of_games, player_wins_grand_total, player_grand_probs, \
        hand_type_wins_grand_total, hand_type_hands_grand_total, \
        hand_type_grand_probs, hand_type_grand_probs2, hole_hand_wins_grand_total, \
        hole_hand_tied_wins_grand_total, hole_hand_hands_grand_total, \
        hole_hand_grand_probs, hole_hand_grand_probs2, hole_hand_norm_grand_probs, \
        hole_hand_rel_grand_probs, hole_hand_rel_grand_probs2
###############################################################################
#######      Get Player List from Dictionary ##################################
###############################################################################

def getPlayerList(player_probs):
    player_probs_list = [player_probs[player] for player in player_probs.keys()]
    return player_probs_list 



###############################################################################
################  Sort HandType Probabilities #################################   
###############################################################################
    
def getHandTypeProbsSorted():

    hand_type_probs_sorted = np.sort(list(hand_type_probs.values()))

    hand_type_keys_sorted = []
    for hand_type_prob_sorted in hand_type_probs_sorted:
        for key in hand_type_probs.keys():
            if hand_type_probs[key] == hand_type_prob_sorted:
                hand_type_keys_sorted.append(key)
                break
            
    hand_type_probs2_sorted = []
    for key in hand_type_keys_sorted:
        hand_type_probs2_sorted.append(hand_type_probs2[key])
            
    return hand_type_keys_sorted, hand_type_probs_sorted, hand_type_probs2_sorted
    
def getWinningHandProbs(hand_type_probs, hand_type_probs2):
    hand_type_cum_probs_sorted = []   
    for i, handType in enumerate(hand_types):
        if i == 0:
            hand_type_cum_probs_sorted.append(hand_type_probs[handType])
        elif i > 0:     
            hand_type_cum_probs_sorted.append(hand_type_probs[handType] \
                + hand_type_cum_probs_sorted[i-1])
    
    hand_type_probs_sorted, hand_type_probs2_sorted, \
        average_winning_hand_type_prob_sorted = [],[],[]
    for i, handType in enumerate(hand_types):
        hand_type_probs_sorted.append(hand_type_probs[handType])
        hand_type_probs2_sorted.append(hand_type_probs2[handType])
        if i == 0:
            average_winning_hand_type_prob_sorted.append(\
                hand_type_probs[handType] * hand_type_probs2[handType])
        elif i > 0:
            average_winning_hand_type_prob_sorted.append(\
                hand_type_probs[handType]*hand_type_probs2[handType] + \
                hand_type_cum_probs_sorted[i-1])

    return hand_type_probs_sorted, hand_type_probs2_sorted, \
        average_winning_hand_type_prob_sorted, hand_type_cum_probs_sorted
        
        

###############################################################################
####  Calculate Surface Coordinates for Rel Prob Plots    #####################
###############################################################################

def getNonPairCombination(hole_hand, low_card, high_card):
    low_card.append(card_rank_numbers[hole_hand[0:1]])
    high_card.append(card_rank_numbers[hole_hand[1:2]])
    return low_card, high_card 

def getPairCombination(hole_hand, pair_card):
    pair_card.append(card_rank_numbers[hole_hand[0:1]])
    return pair_card    

def getCardLabels():
    low_card_labels,high_card_labels = [],[]
    for card in card_ranks:
        if card != 'A':
            low_card_labels.append(card)
        if card != '2':
            high_card_labels.append(card)
    return low_card_labels, high_card_labels
    
def getCoordinatesForSurfaces(hole_hand_rel_probs):

    pair_card, low_card, high_card = [],[],[]   
    rel_probsP, rel_probsS, rel_probsNS = [],[],[]
    for holeHand in permutations:
        if len(holeHand) > 2:      
            if holeHand[2:] == 'S':
                low_card, high_card = getNonPairCombination(holeHand, low_card, high_card)
                rel_probsS.append(hole_hand_rel_probs[holeHand])
            elif holeHand[2:] == 'NS':
                rel_probsNS.append(hole_hand_rel_probs[holeHand])
        elif len(holeHand) == 2:
            pair_card = getPairCombination(holeHand, pair_card)
            rel_probsP.append(hole_hand_rel_probs[holeHand])

    pair_card1, pair_card2, rel_probsP_ribbon = [],[],[]        
    for rank, prob in zip(pair_card, rel_probsP):
        rank_H = rank + .25
        pair_card1.append(rank)        
        pair_card2.append(rank)        
        rel_probsP_ribbon.append(prob)
        pair_card1.append(rank)        
        pair_card2.append(rank_H)        
        rel_probsP_ribbon.append(prob)
        
    return low_card, high_card, rel_probsS, rel_probsNS, pair_card1, pair_card2,\
        rel_probsP_ribbon

###############################################################################
##### Sort Relative Probailities and Create %not Played & %Possible Wins based
##### on sorted Relative Probability1
###############################################################################

def getRelProbsSorted(hole_hand_rel_probs, hole_hand_rel_probs2):

    rel_probs_sorted = np.sort(list(hole_hand_rel_probs.values()))

    rel_probs_keys_sorted = []
    for rel_prob_sorted in rel_probs_sorted:
        for key in hole_hand_rel_probs.keys():
            if hole_hand_rel_probs[key] == rel_prob_sorted:
                rel_probs_keys_sorted.append(key)
                break
        
    rel_probs2_sorted = []
    for key in rel_probs_keys_sorted:
        rel_probs2_sorted.append(hole_hand_rel_probs2[key])
        
    return rel_probs_keys_sorted, rel_probs_sorted, rel_probs2_sorted

def getHoleHandProbs():    
    hole_hand_type_probs = {}
    for holeHand in permutations:
        if len(holeHand) == 2:
            hole_hand_type_probs[holeHand] = 6/1326 
        elif holeHand[2:] == 'S':
            hole_hand_type_probs[holeHand] = 4/1326
        elif holeHand[2:] == 'NS':
            hole_hand_type_probs[holeHand] = 12/1326
    return hole_hand_type_probs

def getHoleHandsProbsSorted(rel_probs_keys_sorted,hole_hand_type_probs):        
    hole_hands_type_probs_sorted = []
    for key in rel_probs_keys_sorted:
        for holeHand, hole_hand_prob in hole_hand_type_probs.items():
            if key == holeHand:
                hole_hands_type_probs_sorted.append(hole_hand_prob)
                break
    return hole_hands_type_probs_sorted
    
def getPercentNotPlayed(rel_probs_keys_sorted, hole_hand_type_probs):            
    percent_not_played1 = []
    for i, key in enumerate(rel_probs_keys_sorted):
        if i == 0:
            percent_not_played1.append(hole_hand_type_probs[key])
        elif i > 0:
            percent_not_played1.append(hole_hand_type_probs[key]+percent_not_played1[i-1])
        
    percent_not_played = {key:value for key, value in zip(rel_probs_keys_sorted, \
        percent_not_played1)}
        
    return percent_not_played

def getDistinctHoleHands2ProbsSorted(rel_probs_keys_sorted, hole_hand_probs):
    hole_hand_probs_sorted = []
    for key in rel_probs_keys_sorted:
        for holeHand, hole_hand_prob in hole_hand_probs.items():
            if key == holeHand:
                hole_hand_probs_sorted.append(hole_hand_prob)
                break
    return hole_hand_probs_sorted

def getPercentPossibleWins(rel_probs_keys_sorted, hole_hand_probs_sorted):
    percent_possible_wins1 = []
    for i, key in enumerate(rel_probs_keys_sorted):
        percent_possible_wins1.append(1 - np.sum(\
            [hole_hand_probs_sorted[j] for j in range(i+1)]))

    percent_possible_wins = {key:value for key, value in zip(rel_probs_keys_sorted, \
        percent_possible_wins1)}
    return percent_possible_wins
    
###############################################################################
############   Player Probability Pie Chart ###################################
def getPlayerPieChart(player_probs, player_probs_list, number_of_games, fig_type):
    player_labels=list(player_probs.keys())
    colors=['lightcoral','blue', 'g', 'r', 'c', 'm', 'y', 'orange', 'w']

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(1,1,1)

    ax1.pie(player_probs_list, labels=player_labels,autopct='%1.1f%%',\
        colors=colors)
    
    ax1.set_title('Player Probabilty')

    plt.figtext(.1,.05, str(number_of_games) + ' Games,  ' + \
        str(len(players)) + ' Players')

    p_pc = job_name+ '_'+ str(len(players))+'P_'+str(number_of_games)+'G_PPC' + fig_type+'.SVG'
    p_pc = {'p_pc'+ fig_type: p_pc}
    
    
    fig1.savefig(job_name+ '_'+ str(len(players))+'P_'+str(number_of_games)+'G_PPC' + fig_type+'.SVG')
    fig1.clf()
    return p_pc
    #fig1.show()
    #plugins.clear(fig1)
    #plugins.connect(fig1, plugins.Reset(), plugins.BoxZoom(), plugins.Zoom())
    #p_pc= mpld3.fig_to_dict(fig1)
    
###############################################################################
########### HandType Probability Bar Chart ####################################
###############################################################################
def getHandTypeBarChart(hand_type_probs_sorted1, hand_type_probs2_sorted1, \
    average_winning_hand_type_prob_sorted1, hand_type_cum_probs_sorted1, \
    fig_type, number_of_games):
        
    index = np.arange(len(hand_types))
    bar_width = .2
        
    x_pos = np.arange(.2,9.2,1)

    fig2 = plt.figure(\
        'Winning Hand Type Probability & Probability of Winning Hand, ' \
        + str(len(players)) + ' Players')
    ax2 = fig2.add_axes([0.075, 0.2, 0.85, 0.7])
   
    ax2.bar(left = index, width = bar_width, height = hand_type_probs_sorted1, \
        color = 'b', label='HandType Winning Prob')
    ax2.bar(left = index + bar_width, width = bar_width, \
        height = hand_type_probs2_sorted1, label='Prob of Winning the Winning HandType', \
        color = 'r')
    ax2.bar(left = index + 2 * bar_width, width = bar_width, \
        height = average_winning_hand_type_prob_sorted1, label= \
        'Average Winning HandType Probability', color = 'g') 
    ax2.bar(left=index + 3 * bar_width, width = bar_width, \
        height = hand_type_cum_probs_sorted1, label='Cumulative Probability of HandType', \
        color = 'y')


    ax2.set_xticks(x_pos) 
    ax2.set_xticklabels(hand_types)
    ax2.set_title('Winning HandType & Winning Hand Probabilities')
    ax2.set_ylabel('Probability')

    ax2.legend(loc = (.6,.4), fontsize = 9)

    for label in ax2.xaxis.get_ticklabels():
       label.set_rotation(45)
       label.set_fontsize(9)
       label.set_color('black')
    
    plt.figtext(.1,.05, str(number_of_games) + ' Games,  ' + \
       str(len(players)) + ' Players')
       
    ht_bc = job_name+ '_'+ str(len(players))+'P_'+str(number_of_games) + \
        'G_HTPBC' + fig_type+'.SVG'
        
    fig2.savefig(ht_bc)    
        
    ht_bc = {'ht_bc'+ fig_type: ht_bc}

    plt.clf()
    
    return ht_bc
    
    #fig2.show()
    #plugins.clear(fig2)
    #plugins.connect(fig2, plugins.Reset(), plugins.BoxZoom(), plugins.Zoom())
    #ht_bc= mpld3.fig_to_dict(fig2)
    
def getHandTypeProbTable(hand_type_probs_sorted1, hand_type_probs2_sorted1, \
    average_winning_hand_type_prob_sorted1, hand_type_cum_probs_sorted1, \
    fig_type, number_of_games):
        
    fig13 = plt.figure('HTT')

    ax13 = fig13.add_axes([0.05,.925,.9,.001], label = 'ax13')

    ax13.set_xticks([])
    ax13.set_xticklabels([])

    ax13.set_yticks([])
    ax13.set_yticklabels([])

    clabels = ['HT','W HT P','P W WHT','A WHT P','Cum P']

    data0 = []
    for i, handType in enumerate(hand_types):
        data0_0 = [handType,'%1.3f' % hand_type_probs_sorted1[i],'%1.3f' % \
            hand_type_probs2_sorted1[i],'%1.3f' % \
            average_winning_hand_type_prob_sorted1[i],'%1.3f' % \
            hand_type_cum_probs_sorted1[i]]
        data0.append(data0_0)

    ht1 = plt.table(colLabels=clabels, cellText = data0, loc = 'bottom',\
        fontsize = 10)
    ax13.add_table(ht1)

    ht_pt = job_name+ '_'+ str(len(players))+'P_'+str(number_of_games)+'G_HTT'+ fig_type + '.SVG'
    fig13.savefig(ht_pt)
    ht_pt = {'ht_pt'+ fig_type: ht_pt}
    
    plt.clf()
    
    return ht_pt
    
    #fig13.show()
    #ht_pt= mpld3.fig_to_dict(fig13)
    
###############################################################################
##############  Relative Probaility Surface Plot ##############################
###############################################################################
def getDataFromCardRanks(rel_probs_data):
    output = []
    cnt = 0
    for i, cardI in enumerate(card_ranks):
        rel_probs = []
        if i == len(card_ranks) - 1:
            break
        output.append(rel_probs)
        for j in range(i+1, len(card_ranks)):
            rel_probs.append(rel_probs_data[cnt])
            cnt+=1
        for j in range(0,i):
            rel_probs.append(0)
    return output
    
    #for i, x in enumerate(x_data):
        #rel_probs = []
        #output.append(rel_probs)
        #for i, y in enumerate(y_data):
            #rel_probs.append(rel_probs_data)

    
def getSurfacePlot(rel_probsS, rel_probsNS, rel_probsP_ribbon,\
    number_of_games, fig_type):
    
    fig4 = plt.figure('Relative Probability by HoleHand')
    ax4= fig4.gca(projection='3d')

    ax4.plot_trisurf(pair_card1, pair_card2, rel_probsP_ribbon, color = 'lightgreen')
    ax4.plot_trisurf(low_card, high_card, rel_probsS,color = 'blue')
    ax4.plot_trisurf(low_card, high_card, rel_probsNS, color = 'red')

    x_pos_L = x_pos_H = np.arange(2,15,1)
    
    ax4.set_xticks(x_pos_L)
    ax4.set_xticklabels(card_ranks)

    ax4.set_yticks(x_pos_H)
    ax4.set_yticklabels(card_ranks)

    ax4.set_title('Relative Winning Probabilities by HoleHandType')
    ax4.set_xlabel('Low Card')
    ax4.set_ylabel('High Card')
    ax4.set_zlabel('Relative Winning Probability')

    lightgreen_patch = mpatches.Patch(color='lightgreen', label='Paired')
    blue_patch = mpatches.Patch(color='blue', label='NonPaired Suited')
    red_patch = mpatches.Patch(color='red', label='NonPaired NonSuited')

    plt.legend(handles = [lightgreen_patch, blue_patch, red_patch], fontsize = 10,\
        loc = (.65,.75))
    
    plt.figtext(.1,.05, str(number_of_games) + ' Games,  ' + \
        str(len(players)) + ' Players')
        
    rel_probs = job_name+ '_'+ str(len(players))+'P_'+str(number_of_games)+ \
        'G_RPSP'+fig_type+'.svg'
    fig4.savefig(rel_probs)
    rel_probs = {'rel_probs'+fig_type: rel_probs}
    
    plt.clf()
    
    return rel_probs
    
    
    #fig4.show()
    #rel_probs_s = getDataFromCardRanks(rel_probsS)
    #plugins.clear(fig4)
    #plugins.connect(fig4, plugins.Reset(), plugins.BoxZoom(), plugins.Zoom())    
    #sp= mpld3.fig_to_dict(fig4)
    
    
    
def getRelProbTable(hole_hand_rel_probs, fig_type):
    fig12 = plt.figure('Relative Probability Table')

    ax12_0 = fig12.add_axes([0.05,.925,.9,.001], label = 'ax12_0')

    ax12_0.set_xticks([])
    ax12_0.set_xticklabels([])

    ax12_0.set_yticks([])
    ax12_0.set_yticklabels([])

    ax12_0.set_title('Relative Probability: Paired')

    clabels0 = card_ranks

    data0 = [[str('%1.1f' % hole_hand_rel_probs[rank+rank])\
        for rank in card_ranks]]
        
    rp0 = plt.table(colLabels=clabels0, cellText = data0, loc = 'bottom', \
        fontsize = 10)
     
    ax12_0.add_table(rp0)


    ax12_1 =fig12.add_axes([0.05,.8,.831,.001],label = 'ax12_1')

    ax12_1.set_xticks([])
    ax12_1.set_xticklabels([])

    ax12_1.set_yticks([])
    ax12_1.set_yticklabels([])

    ax12_1.set_title('Relative Probability: NonPaired Suited')

    clabels1 = [rank for rank in card_ranks if rank != 'A']
    rlabels1 = [rank for rank in card_ranks if rank != '2']
    rlabels1.reverse()

    data1 = []
    for rankH in rlabels1:
        data1_0 = []
        for rankL in clabels1:
            if rankL == rankH:
                while len(data1_0) < len(clabels1):
                    data1_0.append('')               
                break
            else:
                data1_0.append(str('%1.1f' % hole_hand_rel_probs[rankL +\
                    rankH + 'S']))
        data1.append(data1_0)
        
            
    rp1 = plt.table(colLabels=clabels1,rowLabels=rlabels1, cellText = data1, \
        loc = 'bottom',fontsize = 10)
    ax12_1.add_table(rp1)


    ax12_2 =fig12.add_axes([0.05,.375,.831,.001],label = 'ax12_2')

    ax12_2.set_xticks([])
    ax12_2.set_xticklabels([])

    ax12_2.set_yticks([])
    ax12_2.set_yticklabels([])

    ax12_2.set_title('Relative Probability: NonPaired NonSuited')

    clabels2 = [rank for rank in card_ranks if rank != 'A']
    rlabels2 = [rank for rank in card_ranks if rank != '2']
    rlabels2.reverse()

    data2 = []
    for rankH in rlabels2:
        data2_0 = []
        for rankL in clabels2:
            if rankL == rankH:
                while len(data2_0) < len(clabels2):
                    data2_0.append('')               
                break
            else:
                data2_0.append(str('%1.1f' % hole_hand_rel_probs[rankL +\
                    rankH + 'NS']))
        data2.append(data2_0)
        
    rp2 = plt.table(colLabels=clabels2,rowLabels=rlabels2, cellText = data2, \
        loc = 'bottom',fontsize = 10)
    ax12_2.add_table(rp2)


    rel_probs_t = job_name+ '_'+ str(len(players))+'P_'+str(total_number_of_games2)+'G_RPT' + fig_type + '.SVG'
    fig12.savefig(rel_probs_t)
    rel_probs_t = {'rel_probs_t'+fig_type: rel_probs_t}
    plt.clf()
    return rel_probs_t
    
    #fig12.show()
    #rp_t= mpld3.fig_to_dict(fig12)
    
###############################################################################
##########  Suit NonPaired Contour Plot #######################################
###############################################################################
def getSuitedNonPairedContourPlot( number_of_games, fig_type):
    fig5 = plt.figure('Suited NonPaired Relative Probability by HoleHand')
    ax5 = fig5.add_axes([0.1, 0.1, 0.8, 0.8])

    csf = ax5.tricontourf(low_card,high_card, rel_probsS,12)
    cs = ax5.tricontour(low_card, high_card, rel_probsS,12)

    ax5.clabel(cs, cs.levels, inline=True,  fontsize=10,colors='black')
    ax5.grid(True, linestyle="-")

    ax5.plot([2,13],[3,14],color='black')

    x_pos_L = np.arange(2,14,1)
    x_pos_H = np.arange(3,15,1)

    ax5.set_xticks(x_pos_L)
    ax5.set_xticklabels(low_card_labels)

    ax5.set_yticks(x_pos_H)
    ax5.set_yticklabels(high_card_labels)

    cbar = fig5.colorbar(csf, ticks = csf.levels, orientation = 'horizontal')
    cbar.ax.set_xticklabels(csf.levels)

    ax5.set_title('Relative Winning Probabilities by Suited NonPaired HoleHand')
    ax5.set_xlabel('Low Card')
    ax5.set_ylabel('High Card')

    plt.figtext(.1,.05, str(number_of_games) + ' Games,  ' + \
        str(len(players)) + ' Players')

    s_np_cp = job_name+ '_'+ str(len(players))+'P_'+str(number_of_games)+'G_RPSNPCP' + fig_type + '.svg'
    fig5.savefig(s_np_cp)
    s_np_cp = {'s_np_cp'+fig_type: s_np_cp}
    plt.clf()
    return s_np_cp
    
    #fig5.show()
    #s_np_cp= mpld3.fig_to_dict(fig5)
    
###############################################################################
##########  NonSuit NonPaired Contour Plot ####################################
###############################################################################
def getNonSuitedNonPairedContourPlot(number_of_games, fig_type):
    
    fig6 = plt.figure('NonSuited NonPaired Relative Probability by HoleHand')
    ax6 = fig6.add_axes([0.1, 0.1, 0.8, 0.8])

    csf = ax6.tricontourf(low_card, high_card, rel_probsNS,12)
    cs = ax6.tricontour(low_card, high_card, rel_probsNS,12)

    ax6.clabel(cs, cs.levels, inline=True,  fontsize=10,colors='black')
    ax6.grid(True, linestyle="-")

    ax6.plot([2,13],[3,14],color='black')

    x_pos_L = np.arange(2,14,1)
    x_pos_H = np.arange(3,15,1)

    ax6.set_xticks(x_pos_L)
    ax6.set_xticklabels(low_card_labels)

    ax6.set_yticks(x_pos_H)
    ax6.set_yticklabels(high_card_labels)

    cbar = fig6.colorbar(csf, ticks = csf.levels, orientation = 'horizontal')
    cbar.ax.set_xticklabels(csf.levels)

    ax6.set_title('Relative Winning Probabilities by NonSuited NonPaired HoleHand')
    ax6.set_xlabel('Low Card')
    ax6.set_ylabel('High Card')

    plt.figtext(.1,.05, str(number_of_games) + ' Games,  ' + \
        str(len(players)) + ' Players')
 
    ns_np_cp = job_name+ '_'+ str(len(players))+'P_'+str(number_of_games)+'G_RPNSNPCP'+fig_type+'.svg'
    fig6.savefig(ns_np_cp)
    ns_np_cp = {'ns_np_cp'+fig_type: ns_np_cp}
    
    plt.clf()
    return ns_np_cp
    
    #fig6.show()
    #ns_np_cp= mpld3.fig_to_dict(fig6)
    
###############################################################################
##########  NonSuit NonPaired Contour Plot ####################################
###############################################################################
def getPairedContourPlot(number_of_games, fig_type):
    fig7 = plt.figure('Paired Relative Probability by HoleHand')
    ax7 = fig7.add_axes([0.1, 0.1, 0.8, 0.8])

    csf = ax7.tricontourf(pair_card1, pair_card2, rel_probsP_ribbon,12)
    ax7.tricontour(pair_card1, pair_card2, rel_probsP_ribbon,12)
    ax7.plot([2,14],[2,14],color='black')

    ax7.grid(True, linestyle="-")

    x_pos_L = x_pos_H = np.arange(2,15,1)
    
    ax7.set_xticks(x_pos_L)
    ax7.set_xticklabels(card_ranks)

    ax7.set_yticks(x_pos_H)
    ax7.set_yticklabels(card_ranks)

    cbar = fig7.colorbar(csf, ticks = csf.levels, orientation = 'horizontal')
    cbar.ax.set_xticklabels(csf.levels)

    ax7.set_title('Relative Winning Probabilities by Paired HoleHand')
    ax7.set_xlabel('Card 1')
    ax7.set_ylabel('Card 2')

    plt.figtext(.1,.05, str(number_of_games) + ' Games,  ' + \
        str(len(players)) + ' Players')
 
    
    p_cp = job_name+ '_'+ str(len(players))+'P_'+str(number_of_games)+'G_RPPCP'+ fig_type+'.svg' 
    fig7.savefig(p_cp )
    p_cp = {'p_cp'+fig_type:p_cp}
    
    plt.clf()
    return p_cp
    
    #fig7.show()
    #p_cp= mpld3.fig_to_dict(fig7)

###############################################################################
#####  Relative Probability Bar Chart #########################################    
###############################################################################
def getRelProbBarChart(rel_probs_keys_sorted, rel_probs_sorted, rel_probs2_sorted, number_of_games, fig_type):
    index = np.arange(len(rel_probs_keys_sorted))
    bar_width = .5

    fig8 = plt.figure('Rel Prob & Rel Prob2 By Hand Type')
    ax8 = fig8.add_axes([.07,.1,.9,.85])

    ax8.bar(left = index, width = bar_width, height = rel_probs_sorted,\
        color = 'blue', label = 'Rel_Prob_1')

    ax8.bar(left = index + bar_width, width = bar_width,\
        height = rel_probs2_sorted, color = 'red', label = 'Rel_Prob_2')
    
    ax8.set_title('Sorted Winning Relative Probability(1&2) by HoleHand, ' + \
        str(number_of_games) + ' Games, ' + str(len(players)) + \
        ' Players',fontsize = 10)
    
    xticks1 = np.arange(0,184.8,16.8)
    xticklabels = [x/168 for x in xticks1]
    ax8.set_xticks(xticks1)
    ax8.set_xticklabels(labels = xticklabels, fontsize = 10)
    ax8.set_xlabel('% of Sorted HoleHands',fontsize = 10)

    yticks1 = np.arange(0,3,.5)
    yticklabels = [y for y in yticks1]
    ax8.set_yticks(yticks1)
    ax8.set_yticklabels(labels = yticklabels, fontsize = 10)
    ax8.set_ylabel('Winning Relative Probability(1&2)',fontsize = 10)

    ax8.legend(fontsize = 10, loc = (.05,.85))
    
    
    rp_bc = job_name+ '_'+ str(len(players))+'P_'+str(number_of_games)+'G_RPBC' + fig_type + '.svg'
    fig8.savefig(rp_bc)
    rp_bc = {'rp_bc'+fig_type:rp_bc}
    
    plt.clf()
    return rp_bc
    
    #fig8.show()
    #rp_bc= mpld3.fig_to_dict(fig8)

###############################################################################
######  Scatter Plot: Relative Probability 2 to Relative Probability
###############################################################################
def getRelProbScatterPlot(rel_probs3_x, rel_probs3_y, number_of_games, fig_type):
    fig9 = plt.figure('Relative Probability Vs. Relative Probability 2')
    ax9 = fig9.add_axes([0.1, 0.2, 0.8, 0.7])

    ax9.plot(rel_probs3_x, rel_probs3_y,'bo')

    ax9.set_title(\
        'Winning Relative Probability2 vs. by Winning Relative Probability1, '\
        + str(len(players)) + ' Players', fontsize = 10)
    ax9.set_xlabel('Winning Relative Probability1')
    ax9.set_ylabel('Winning Relative Probability2')

    plt.figtext(.1,.05, str(number_of_games) + ' Games,  ' + \
        str(len(players)) + ' Players')

    rp_sp = job_name+ '_'+ str(len(players))+'P_'+str(number_of_games)+'G_RPSCP' + fig_type + '.svg'
    fig9.savefig(rp_sp)
    rp_sp = {'rp_sp'+fig_type:rp_sp}
    plt.clf()
    return rp_sp

    #fig9.show()
    #rp_sp= mpld3.fig_to_dict(fig9
###############################################################################
###### Plot, Percent Possible Wins vs. Percent Not Played, Sort by Rel Prob
###############################################################################
def getPossibleWinsData(hole_hand_rel_probs, hole_hand_rel_probs2, hole_hand_probs):
    rel_probs_keys_sorted, rel_probs_sorted, rel_probs2_sorted = \
    getRelProbsSorted(hole_hand_rel_probs, hole_hand_rel_probs2)
    hole_hand_type_probs = getHoleHandProbs()
    hole_hand_probs_sorted = \
        getDistinctHoleHands2ProbsSorted(rel_probs_keys_sorted,\
        hole_hand_probs)    
    percent_not_played = getPercentNotPlayed(rel_probs_keys_sorted, hole_hand_type_probs)
    percent_possible_wins = \
        getPercentPossibleWins(rel_probs_keys_sorted,hole_hand_probs_sorted)

    percent_not_played_x = [percent_not_played[key]*100 for key in rel_probs_keys_sorted]
    percent_possible_wins_y = [percent_possible_wins[key]*100 for key in \
        rel_probs_keys_sorted]
    
    return percent_not_played_x, percent_possible_wins_y 

def getPossibleWinsPlot(percent_not_played_x, percent_possible_wins_y, number_of_games, fig_type):
    fig10 = plt.figure('Percent Possible Wins Vs. Percent Not Played')
    ax10 = fig10.add_axes([.1,.2,.8,.7])

    ax10.plot(percent_not_played_x, percent_possible_wins_y,'bo')
    ax10.grid(True, linestyle="-")

    ax10.set_title('Percent Possible Wins vs. Percent Not Played')
    ax10.set_xlabel('Percent Not Played')
    ax10.set_ylabel('Percent Possible Wins')

    plt.figtext(.1,.05, str(number_of_games) + ' Games,  ' + \
        str(len(players)) + ' Players')
       
    pw_p = job_name+ '_'+ str(len(players))+'P_'+str(number_of_games)+'G_PWPNPSCP' + fig_type + '.svg'
    fig10.savefig(pw_p)
    pw_p = {'pw_p'+fig_type:pw_p}
    plt.clf()
    return pw_p
    
    #fig10.show()
    #pw_p= mpld3.fig_to_dict(fig10)

def getPossibleWinsTable(percent_not_played_x,percent_possible_wins_y, \
    rel_probs_keys_sorted, number_of_games, fig_type):
    fig11 = plt.figure('PercentPossibleWins vs. PercentNotPlayed Table')

    ax11_0 = fig11.add_axes([0.0125,.025,.175,.001], label = 'ax11_0')

    clabels = ['HH Type','%NP','%PW']

    ax11_0.set_xticks([])
    ax11_0.set_xticklabels([])

    ax11_0.set_yticks([])
    ax11_0.set_yticklabels([])

    data0 = [[key,str('%1.0f' % percent_not_played_x[i]),\
        str('%1.0f' % percent_possible_wins_y[i])] \
        for i, key in enumerate(rel_probs_keys_sorted) if i < 33]
    data0.insert(0,['','0','1'])
    wnp0 = plt.table(colLabels=clabels, cellText = data0, loc = 'top',fontsize = 10)
    ax11_0.add_table(wnp0)

    ax11_1 =fig11.add_axes([.2125,.025,.175,.001],label = 'ax11_1')

    ax11_1.set_xticks([])
    ax11_1.set_xticklabels([])

    ax11_1.set_yticks([])
    ax11_1.set_yticklabels([])

    data1 = [[key,str('%1.0f' % percent_not_played_x[i]),\
        str('%1.0f' % percent_possible_wins_y[i])] \
        for i, key in enumerate(rel_probs_keys_sorted) if 32 < i and i <67]
    wnp1 = plt.table(colLabels=clabels, cellText = data1, loc = 'top',fontsize = 10)
    ax11_1.add_table(wnp1)


    ax11_2 =fig11.add_axes([.4125,.025,.175,.001],label = 'ax11_2')

    ax11_2.set_xticks([])
    ax11_2.set_xticklabels([])

    ax11_2.set_yticks([])
    ax11_2.set_yticklabels([])

    data2 = [[key,str('%1.0f' % percent_not_played_x[i]),\
        str('%1.0f' % percent_possible_wins_y[i])] \
        for i, key in enumerate(rel_probs_keys_sorted) if 66 < i and i <101]
    wnp2 = plt.table(colLabels=clabels, cellText = data2, loc = 'top',fontsize = 10)
    ax11_2.add_table(wnp2)

    ax11_3 =fig11.add_axes([.6125,.025,.175,.001],label = 'ax11_3')

    ax11_3.set_xticks([])
    ax11_3.set_xticklabels([])

    ax11_3.set_yticks([])
    ax11_3.set_yticklabels([])

    data3 = [[key,str('%1.0f' % percent_not_played_x[i]),\
        str('%1.0f' % percent_possible_wins_y[i])] \
        for i, key in enumerate(rel_probs_keys_sorted) if 100 < i and i <135]
    wnp3 = plt.table(colLabels=clabels, cellText = data3, loc = 'top',fontsize = 10)
    ax11_3.add_table(wnp3)

    ax11_4 =fig11.add_axes([.8125,.025,.175,.001],label = 'ax11_4')

    ax11_4.set_xticks([])
    ax11_4.set_xticklabels([])

    ax11_4.set_yticks([])
    ax11_4.set_yticklabels([])

    data4 = [[key,str('%1.0f' % percent_not_played_x[i]),\
        str('%1.0f' % percent_possible_wins_y[i])] \
        for i, key in enumerate(rel_probs_keys_sorted) if 134 < i and i <169]
    wnp4 = plt.table(colLabels=clabels, cellText = data4, loc = 'top',fontsize = 10)
    ax11_4.add_table(wnp4)

    pw_t = job_name+ '_'+ str(len(players))+'P_'+str(number_of_games)+'G_PWPNPT' + fig_type + '.svg'
    fig11.savefig(pw_t)
    pw_t = {'pw_t'+fig_type:pw_t}
    plt.clf()
    return pw_t
    
    #fig11.show()
    #pw_t= mpld3.fig_to_dict(fig11)
def put_analyzed_data(analyzed_job_data, job_name, total_number_of_games2, \
    grand_total_number_of_games):
    
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])    
        cur = cnx.cursor()
        update_analyze_jobs = ("update gamesim_analyzed_jobs "
                    "set analyzed_job_data = %(analyzed_job_data)s, "
                    "num_games = %(num_games)s, "
                    "grand_num_games = %(grand_num_games)s "
                    "where job_name = %(job_name)s;")
        
        update_data = {'job_name': job_name, \
                'analyzed_job_data': analyzed_job_data,
                'num_games': total_number_of_games2,
                'grand_num_games': grand_total_number_of_games}
                    
        cur.execute(update_analyze_jobs, update_data)
                    
        cnx.commit() 
        cnx.close()
    
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
    
    return
    
def update_status(status_parameter, job_name):
    
    try:    
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])    
        cur = cnx.cursor()
        
        if status_parameter == 1:
            update_analyze_job_status = ("update gamesim_analyze_job_status "
                            "set p_pc_status = 'running' "
                            "where job_name = %(job_name)s;")
        elif status_parameter == 2:
            update_analyze_job_status = ("update gamesim_analyze_job_status "
                            "set p_pc_status = 'finished', "
                            "ht_bc_status = 'running' "
                            "where job_name = %(job_name)s;")                                
        elif status_parameter == 3:
            update_analyze_job_status = ("update gamesim_analyze_job_status "
                            "set ht_bc_status = 'finished', "
                            "ht_pt_status = 'running' "
                            "where job_name = %(job_name)s;")                               
        elif status_parameter == 4:
            update_analyze_job_status = ("update gamesim_analyze_job_status "
                            "set ht_pt_status = 'finished', "
                            "sp_status = 'running' "
                            "where job_name = %(job_name)s;")                                
        elif status_parameter == 5:
            update_analyze_job_status = ("update gamesim_analyze_job_status "
                            "set sp_status = 'finished', "
                            "rp_t_status = 'running' "
                            "where job_name = %(job_name)s;")                                
        elif status_parameter == 6:
            update_analyze_job_status = ("update gamesim_analyze_job_status "
                            "set rp_t_status = 'finished', "
                            "s_np_cp_status = 'running' "
                            "where job_name = %(job_name)s;")                                
        elif status_parameter == 7:
            update_analyze_job_status = ("update gamesim_analyze_job_status "
                            "set s_np_cp_status = 'finished', "
                            "ns_np_cp_status = 'running' "
                            "where job_name = %(job_name)s;")                                
        elif status_parameter == 8:
            update_analyze_job_status = ("update gamesim_analyze_job_status "
                            "set ns_np_cp_status = 'finished', "
                            "p_cp_status = 'running' "
                            "where job_name = %(job_name)s;")                                
        elif status_parameter == 9:
            update_analyze_job_status = ("update gamesim_analyze_job_status "
                            "set p_cp_status = 'finished', "
                            "rp_bc_status = 'running' "
                            "where job_name = %(job_name)s;")                                
        elif status_parameter == 10:
            update_analyze_job_status = ("update gamesim_analyze_job_status "
                            "set rp_bc_status = 'finished', "
                            "rp_sp_status = 'running' "
                            "where job_name = %(job_name)s;")                                
        elif status_parameter == 11:
            update_analyze_job_status = ("update gamesim_analyze_job_status "
                            "set rp_sp_status = 'finished', "
                            "pw_p_status = 'running' "
                            "where job_name = %(job_name)s;")
        elif status_parameter == 12:
            update_analyze_job_status = ("update gamesim_analyze_job_status "
                            "set pw_p_status = 'finished', "
                            "pw_t_status = 'running' "
                            "where job_name = %(job_name)s;")                                
        elif status_parameter == 13:
            update_analyze_job_status = ("update gamesim_analyze_job_status "
                            "set pw_t_status = 'finished' "
                            "where job_name = %(job_name)s;")
                            
        update_data = {'job_name': job_name}                            
        cur.execute(update_analyze_job_status, update_data)
        
        cnx.commit() 
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
    
        update_simulation_job = ("update gamesim_analyzed_jobs "
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
#####  Get Summary Data #######################################################       
###############################################################################

db_params = {'username':'texasholdem', 'password': 'Texasholdem123', \
    'database': 'texasholdem_db'}

root_dir = 'C:\\Source\\TexasHoldem\\'
#root_dir = 'C:\\'
analyze_id = sys.argv[1]
run_time = get_run_time(analyze_id)
job_name = 'analyze' + str(sys.argv[1])

#data_dir = '\\static\\img\\'
data_dir = 'gamesim\\static\\img\\'
os.chdir(root_dir + data_dir)

set_global_sql_variables()

#os.chdir(root_dir)
#from gamesim.models import analyze_job_status
#aj1 = create_analyze_job_status()
analyzed_job_data = []
        
players, card_suits, card_ranks, card_rank_numbers, hand_types, \
    hand_type_ranks, permutations, total_number_of_games2, player_wins_total, \
    player_probs, hand_type_wins_total, hand_type_hands_total, \
    hand_type_probs, hand_type_probs2, hole_hand_wins_total, \
    hole_hand_tied_wins_total, hole_hand_hands_total, hole_hand_probs, \
    hole_hand_probs2, hole_hand_norm_probs, hole_hand_rel_probs, \
    hole_hand_rel_probs2, grand_total_number_of_games, player_wins_grand_total, \
    player_grand_probs, hand_type_wins_grand_total, hand_type_hands_grand_total, \
    hand_type_grand_probs, hand_type_grand_probs2, hole_hand_wins_grand_total, \
    hole_hand_tied_wins_grand_total, hole_hand_hands_grand_total, hole_hand_grand_probs, \
    hole_hand_grand_probs2, hole_hand_norm_grand_probs, hole_hand_rel_grand_probs, \
    hole_hand_rel_grand_probs2 = getSummaryData(job_name)
    
player_probs_list = getPlayerList(player_probs)
player_grand_probs_list = getPlayerList(player_grand_probs)

update_status(1, job_name)

p_pc_job = getPlayerPieChart(player_probs, player_probs_list, \
    total_number_of_games2, '_job')
    
analyzed_job_data.append(p_pc_job)

p_pc_gt = getPlayerPieChart(player_grand_probs, player_grand_probs_list, \
    grand_total_number_of_games, '_gt')
    
analyzed_job_data.append(p_pc_gt)
    
update_status(2, job_name)

hand_type_probs_sorted, hand_type_probs2_sorted, \
    average_winning_hand_type_prob_sorted, hand_type_cum_probs_sorted = \
    getWinningHandProbs(hand_type_probs, hand_type_probs2)
    
hand_type_grand_probs_sorted, hand_type_grand_probs2_sorted, \
    average_winning_hand_type_grand_prob_sorted, \
    hand_type_cum_grand_probs_sorted = \
    getWinningHandProbs(hand_type_grand_probs, hand_type_grand_probs2)
    
ht_bc_job = getHandTypeBarChart(hand_type_probs_sorted, hand_type_probs2_sorted, \
    average_winning_hand_type_prob_sorted, hand_type_cum_probs_sorted, \
    '_job', total_number_of_games2) 
    
analyzed_job_data.append(ht_bc_job)
    
ht_bc_gt = getHandTypeBarChart(hand_type_grand_probs_sorted, hand_type_grand_probs2_sorted, \
    average_winning_hand_type_grand_prob_sorted, hand_type_cum_grand_probs_sorted, \
    '_gt', grand_total_number_of_games)
    
analyzed_job_data.append(ht_bc_gt)    

update_status(3, job_name)

ht_pt_job = getHandTypeProbTable(hand_type_probs_sorted, hand_type_probs2_sorted, \
    average_winning_hand_type_prob_sorted, hand_type_cum_probs_sorted, \
    '_job', total_number_of_games2)
    
analyzed_job_data.append(ht_pt_job)

ht_pt_gt = getHandTypeProbTable(hand_type_grand_probs_sorted, hand_type_grand_probs2_sorted, \
    average_winning_hand_type_grand_prob_sorted, hand_type_cum_grand_probs_sorted, \
    '_gt', grand_total_number_of_games)
    
analyzed_job_data.append(ht_pt_gt)
    
update_status(4, job_name)

low_card, high_card, rel_probsS, rel_probsNS, pair_card1, pair_card2,\
    rel_probsP_ribbon = getCoordinatesForSurfaces(hole_hand_rel_probs)
    
rel_probs_job = getSurfacePlot( rel_probsS, rel_probsNS, rel_probsP_ribbon, \
    total_number_of_games2, '_job')

analyzed_job_data.append(rel_probs_job)

low_card, high_card, rel_grand_probsS, rel_grand_probsNS, pair_card1, pair_card2,\
    rel_grand_probsP_ribbon = getCoordinatesForSurfaces(hole_hand_rel_grand_probs)
    
rel_probs_gt = getSurfacePlot(rel_grand_probsS, rel_grand_probsNS, \
    rel_grand_probsP_ribbon, grand_total_number_of_games, '_gt')

analyzed_job_data.append(rel_probs_gt)

update_status(5, job_name)

rel_prob_t_job = getRelProbTable(hole_hand_rel_probs,'_job')

analyzed_job_data.append(rel_prob_t_job)

rel_prob_t_gt = getRelProbTable(hole_hand_rel_grand_probs,'_gt')

analyzed_job_data.append(rel_prob_t_gt)

update_status(6, job_name)

low_card, high_card, rel_probsS, rel_probsNS, pair_card1, pair_card2,\
    rel_probsP_ribbon = getCoordinatesForSurfaces(hole_hand_rel_probs)

low_card_labels, high_card_labels = getCardLabels()

s_np_cp_job = getSuitedNonPairedContourPlot(total_number_of_games2, '_job')

analyzed_job_data.append(s_np_cp_job)

low_card, high_card, rel_probsS, rel_probsNS, pair_card1, pair_card2,\
    rel_probsP_ribbon = getCoordinatesForSurfaces(hole_hand_rel_grand_probs)

low_card_labels, high_card_labels = getCardLabels()

s_np_cp_gt = getSuitedNonPairedContourPlot(grand_total_number_of_games, '_gt')

analyzed_job_data.append(s_np_cp_gt)

update_status(7, job_name)

low_card, high_card, rel_probsS, rel_probsNS, pair_card1, pair_card2,\
    rel_probsP_ribbon = getCoordinatesForSurfaces(hole_hand_rel_probs)

ns_np_cp_job = getNonSuitedNonPairedContourPlot(total_number_of_games2, '_job')

analyzed_job_data.append(ns_np_cp_job)

low_card, high_card, rel_probsS, rel_probsNS, pair_card1, pair_card2,\
    rel_probsP_ribbon = getCoordinatesForSurfaces(hole_hand_rel_grand_probs)

ns_np_cp_gt = getNonSuitedNonPairedContourPlot(grand_total_number_of_games, '_gt')

analyzed_job_data.append(ns_np_cp_gt)

update_status(8, job_name)

low_card, high_card, rel_probsS, rel_probsNS, pair_card1, pair_card2,\
    rel_probsP_ribbon = getCoordinatesForSurfaces(hole_hand_rel_probs)

p_cp_job = getPairedContourPlot(total_number_of_games2, '_job')

analyzed_job_data.append(p_cp_job)

low_card, high_card, rel_probsS, rel_probsNS, pair_card1, pair_card2,\
    rel_probsP_ribbon = getCoordinatesForSurfaces(hole_hand_rel_grand_probs)

p_cp_gt = getPairedContourPlot(grand_total_number_of_games, '_gt')

analyzed_job_data.append(p_cp_gt)

update_status(9, job_name)


rel_probs_keys_sorted, rel_probs_sorted, rel_probs2_sorted = \
    getRelProbsSorted(hole_hand_rel_probs, hole_hand_rel_probs2)

rp_bc_job = getRelProbBarChart(rel_probs_keys_sorted, rel_probs_sorted, rel_probs2_sorted, \
    total_number_of_games2, '_job')
    
analyzed_job_data.append(rp_bc_job)

rel_grand_probs_keys_sorted, rel_grand_probs_sorted, rel_grand_probs2_sorted = \
    getRelProbsSorted(hole_hand_rel_grand_probs, hole_hand_rel_grand_probs2)

rp_bc_gt = getRelProbBarChart(rel_grand_probs_keys_sorted, \
    rel_grand_probs_sorted, rel_grand_probs2_sorted, \
    grand_total_number_of_games, '_gt')
    
analyzed_job_data.append(rp_bc_gt)

    
update_status(10, job_name)

rel_probs3_x = [hole_hand_rel_probs[key] for key in \
    permutations]
rel_probs3_y = [hole_hand_rel_probs2[key] for key in \
    permutations]
    
rp_sp_job = getRelProbScatterPlot(rel_probs3_x, rel_probs3_y, \
    total_number_of_games2, '_job')

analyzed_job_data.append(rp_sp_job)

rel_grand_probs3_x = [hole_hand_rel_grand_probs[key] for key in \
    permutations]
rel_grand_probs3_y = [hole_hand_rel_grand_probs2[key] for key in \
    permutations]
    
rp_sp_gt = getRelProbScatterPlot(rel_grand_probs3_x, rel_grand_probs3_y, \
    grand_total_number_of_games, '_gt')

analyzed_job_data.append(rp_sp_gt)


update_status(11, job_name)
    
percent_not_played_x, percent_possible_wins_y = \
    getPossibleWinsData(hole_hand_rel_probs, hole_hand_rel_probs2, hole_hand_probs)
    
pw_p_job = getPossibleWinsPlot(percent_not_played_x, percent_possible_wins_y, \
    total_number_of_games2, '_job')

analyzed_job_data.append(pw_p_job)

grand_percent_not_played_x, grand_percent_possible_wins_y = \
    getPossibleWinsData(hole_hand_rel_grand_probs, hole_hand_rel_grand_probs2, \
    hole_hand_grand_probs)
    
pw_p_gt = getPossibleWinsPlot(grand_percent_not_played_x, \
    grand_percent_possible_wins_y, grand_total_number_of_games, '_gt')

analyzed_job_data.append(pw_p_gt)


update_status(12, job_name)

pw_t_job = getPossibleWinsTable(percent_not_played_x,percent_possible_wins_y, \
    rel_probs_keys_sorted, total_number_of_games2, '_job')

analyzed_job_data.append(pw_t_job)

   
update_status(13, job_name)

analyzed_job_data = json.dumps(analyzed_job_data)
put_analyzed_data(analyzed_job_data, job_name, total_number_of_games2, \
    grand_total_number_of_games)

finish_time = dt.datetime.now(pytz.utc)
put_finish_time()    


"""
def getJobName():
    if len(sys.argv) == 1:
        job_name = input('Summary Job Name-->')
    else:
        job_name = sys.argv[1]
    return job_name
    
def getWorkingDir():
    if len(sys.argv) == 2:
        work_dir = input('Working Dir-->')
    else:
        work_dir = sys.argv[2]
    return work_dir
"""




    