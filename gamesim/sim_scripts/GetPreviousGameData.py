# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 12:19:40 2015

@author: Larry
"""

import json
#import time
#import sys
import mysql.connector

def getCpuLoopData(rows, cpuLoopData):
    for row in rows: 
        cpuLoopData = getLoopData(row,cpuLoopData)
                
    for loop in cpuLoopData:
        putParentData(loop)
            
        for loop_dicts in loop['nonTiedGames']:
            putNonTiedGames(loop_dicts)
                
        for loop1_dicts in loop['tiedGames']:
            putTiedGames(loop_dicts)
    
    return

def getLoopData(row, cpuLoopData):
    
    cpuLoopData_1 = {}
    cpuLoopData_1['runTime'] = row[1]                        
    cpuLoopData_1['numPlayers'] = row[2]
    cpuLoopData_1['nonTiedGames'] = json.loads(row[4])
    cpuLoopData_1['tiedGames']=json.loads(row[5])
    cpuLoopData_1['parentData'] = json.loads(row[6])
    cpuLoopData.append(cpuLoopData_1)
    
    return cpuLoopData
    
def putParentData(loop):
    loop_dict = {}
    for key, values in loop['parentData'].items():
        loop_dict[key] = values
    loop_dict['runTime'] = loop['runTime']
    loop_dict['numPlayers'] = loop['numPlayers']
    parentData.append(loop_dict)
    
    return parentData
    
def putNonTiedGames(loop_dicts):
    loop_dict = {}
    for key, value in loop_dicts.items():
        loop_dict[key]= value
    NonTiedGames.append(loop_dict)
    
    return NonTiedGames
    
def putTiedGames(loop_dicts):
    loop_dict = {}
    for key, value in loop_dicts.items():
        loop_dict[key]= value
    TiedGames.append(loop_dict)
    
    return TiedGames

def getGameData():
    
    try:
        cpu1LoopData, cpu2LoopData, cpu3LoopData = [], [], []
   
        cnx = mysql.connector.connect(user='texasholdem', password = \
            'Texasholdem123', database='texasholdem')
        
        cur = cnx.cursor()
    
        select_cpu1LoopData = ("select * from cpu1LoopData;")
        select_cpu2LoopData = ("select * from cpu2LoopData;")
        select_cpu3LoopData = ("select * from cpu3LoopData;")
        
        cur.execute(select_cpu1LoopData)
        rows = cur.fetchall()
        getCpuLoopData(rows, cpu1LoopData)
                        
        cur.execute(select_cpu2LoopData)
        rows = cur.fetchall()
        getCpuLoopData(rows, cpu2LoopData)        
        
        cur.execute(select_cpu3LoopData)
        rows = cur.fetchall()       
        getCpuLoopData(rows, cpu3LoopData)        
                
        cnx.close()
        
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])

    return 
    
###############################################################################
############## Get Data from CpuLoop Tables  ##################################
###############################################################################
NonTiedGames, TiedGames, parentData = [], [], []
    
getGameData()


