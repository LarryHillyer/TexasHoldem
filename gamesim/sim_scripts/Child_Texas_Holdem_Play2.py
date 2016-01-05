# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 16:03:35 2015

@author: Larry
"""
import sys
import json
#import numpy as np
from random import shuffle
import mysql.connector

#import datetime as dt
import TexasHoldemInitialize2 as th_i
import BestHands as bh
import Winners as win

    
###############################################################################
###### Update PlayerWins and Game Dictionaries with Game Result   #############
###############################################################################
    
def putPlayerWinsAndGameDictionaries(numberOfTieGames, numberOfNonTieGames, \
    totalNumberOfGames):
    totalNumberOfGames +=1
    if len(Game['Winners']) == 1:
        if Game['Winners'][0] == Players[0]:
            Player_Wins['player0'] +=1
        elif Game['Winners'][0] == Players[1]:
            Player_Wins['player1'] +=1
        elif Game['Winners'][0] == Players[2]:
            Player_Wins['player2'] +=1
        elif Game['Winners'][0] == Players[3]:
            Player_Wins['player3'] +=1
        elif Game['Winners'][0] == Players[4]:
            Player_Wins['player4'] +=1
        elif Game['Winners'][0] == Players[5]:
            Player_Wins['player5'] +=1
        elif Game['Winners'][0] == Players[6]:
            Player_Wins['player6'] +=1
        elif Game['Winners'][0] == Players[7]:
            Player_Wins['player7'] +=1
        numberOfNonTieGames +=1
        NonTiedGames.append(Game)
    elif len(Game['Winners']) > 1:
        numberOfTieGames +=1
        Player_Wins['tied'] +=1
        TiedGames.append(Game)
    
    return numberOfTieGames, numberOfNonTieGames, totalNumberOfGames
    
###############################################################################
###### Update HandTypeWins Dictionary with Game Result   ###############
###############################################################################
def putHandTypeWins():
    if Game['BestHandType'] == 'HighCard':
        HandType_Wins['HighCard'] +=1
    elif Game['BestHandType'] == 'OnePair':
        HandType_Wins['OnePair'] +=1
    elif Game['BestHandType'] == 'TwoPairs':
        HandType_Wins['TwoPairs'] +=1
    elif Game['BestHandType'] == 'ThreeOfAKind':
        HandType_Wins['ThreeOfAKind'] +=1
    elif Game['BestHandType'] == 'Straight':
        HandType_Wins['Straight'] +=1
    elif Game['BestHandType'] == 'Flush':
        HandType_Wins['Flush'] +=1
    elif Game['BestHandType'] == 'FullHouse':
        HandType_Wins['FullHouse'] +=1
    elif Game['BestHandType'] == 'FourOfAKind':
        HandType_Wins['FourOfAKind'] +=1
    elif Game['BestHandType'] == 'StraightFlush':
        HandType_Wins['StraightFlush'] +=1
    
    return 
###############################################################################
###### Update HandTypeHands Dictionary with Game Result   ###############
###############################################################################
def putHandTypeHands():
    for player in Players:
        if BestHands[player][0]['HandType'] == 'HighCard' and \
            Game['BestHandType'] == 'HighCard':
            HandType_Hands['HighCard'] +=1
        elif BestHands[player][0]['HandType'] == 'OnePair' and \
            Game['BestHandType'] == 'OnePair':
            HandType_Hands['OnePair'] +=1
        elif BestHands[player][0]['HandType'] == 'TwoPairs' and \
            Game['BestHandType'] == 'TwoPairs':
            HandType_Hands['TwoPairs'] +=1
        elif BestHands[player][0]['HandType'] == 'ThreeOfAKind' and \
            Game['BestHandType'] == 'ThreeOfAKind':
            HandType_Hands['ThreeOfAKind'] +=1
        elif BestHands[player][0]['HandType'] == 'Straight' and \
            Game['BestHandType'] == 'Straight':
            HandType_Hands['Straight'] +=1
        elif BestHands[player][0]['HandType'] == 'Flush' and \
            Game['BestHandType'] == 'Flush':
            HandType_Hands['Flush'] +=1
        elif BestHands[player][0]['HandType'] == 'FullHouse' and \
            Game['BestHandType'] == 'FullHouse':
            HandType_Hands['FullHouse'] +=1
        elif BestHands[player][0]['HandType'] == 'FourOfAKind' and \
            Game['BestHandType'] == 'FourOfAKind':
            HandType_Hands['FourOfAKind'] +=1
        elif BestHands[player][0]['HandType'] == 'StraightFlush' and \
            Game['BestHandType'] == 'StraightFlush':
            HandType_Hands['StraightFlush'] +=1
    
    return
    
    
###############################################################################
######## Update Tied and NonTiedGame HoleHandWin Dictionaries #################
###############################################################################

def putNonTiedHoleHandWinDictionaries():
    for game in NonTiedGames:
        for player in Players:
            if game['HoleCards'][player][0][0] == \
                game['HoleCards'][player][1][0]:
                DistinctHoleHands2_Hands[game['HoleCards'][player][0][0]+ \
                    game['HoleCards'][player][1][0]] +=1            
                if game['Winners'].__contains__(player):                                                
                   DistinctHoleHands2_Wins[game['HoleCards'][player][0][0]+ \
                       game['HoleCards'][player][1][0]] +=1
            elif game['HoleCards'][player][0][1] == \
                game['HoleCards'][player][1][1] and \
                game['HoleCards'][player][0][0] != \
                game['HoleCards'][player][1][0]:                    
                    if CardRankNumbers[game['HoleCards'][player][0][0]] > \
                        CardRankNumbers[game['HoleCards'][player][1][0]]:
                        nonPair = game['HoleCards'][player][1][0] + \
                            game['HoleCards'][player][0][0] + 'S'
                    else:
                        nonPair = game['HoleCards'][player][0][0] + \
                            game['HoleCards'][player][1][0] + 'S'
                    DistinctHoleHands2_Hands[nonPair] +=1                    
                    if game['Winners'].__contains__(player):                    
                        DistinctHoleHands2_Wins[nonPair] +=1
            elif game['HoleCards'][player][0][1] != \
                game['HoleCards'][player][1][1] and \
                game['HoleCards'][player][0][0] != \
                game['HoleCards'][player][1][0]:
                if CardRankNumbers[game['HoleCards'][player][0][0]] > \
                    CardRankNumbers[game['HoleCards'][player][1][0]]:
                    nonPair = game['HoleCards'][player][1][0] + \
                        game['HoleCards'][player][0][0] + 'NS'
                else:
                    nonPair = game['HoleCards'][player][0][0] + \
                        game['HoleCards'][player][1][0] + 'NS'                                       
                DistinctHoleHands2_Hands[nonPair] +=1                    
                if game['Winners'].__contains__(player):
                    DistinctHoleHands2_Wins[nonPair] +=1
    return
    
def putTiedHoleHandWinDictionaries():
    totalTiedGames =0                   
    for game in TiedGames:
        winnerCnt = 0
        for player in Players:
            if game['HoleCards'][player][0][0] == \
                game['HoleCards'][player][1][0]:
                DistinctHoleHands2_Hands[game['HoleCards'][player][0][0] + \
                    game['HoleCards'][player][1][0]] +=1            
                if game['Winners'].__contains__(player):                                                
                    if winnerCnt == 0:
                        DistinctHoleHands2_TiedWins[\
                            game['HoleCards'][player][0][0] + \
                            game['HoleCards'][player][1][0]] +=1                    
                        winnerCnt +=1
                        totalTiedGames +=1
            elif game['HoleCards'][player][0][1] == \
                game['HoleCards'][player][1][1] and \
                game['HoleCards'][player][0][0] != \
                game['HoleCards'][player][1][0]:                    
                if CardRankNumbers[game['HoleCards'][player][0][0]] > \
                    CardRankNumbers[game['HoleCards'][player][1][0]]:
                    nonPair = game['HoleCards'][player][1][0] + \
                        game['HoleCards'][player][0][0] + 'S'
                else:
                    nonPair = game['HoleCards'][player][0][0] + \
                        game['HoleCards'][player][1][0] + 'S'
                DistinctHoleHands2_Hands[nonPair] +=1                    
                if game['Winners'].__contains__(player):                    
                    if winnerCnt == 0:
                        DistinctHoleHands2_TiedWins[nonPair] +=1
                        winnerCnt +=1
                        totalTiedGames +=1
            elif game['HoleCards'][player][0][1] != \
                game['HoleCards'][player][1][1] and \
                game['HoleCards'][player][0][0] != \
                game['HoleCards'][player][1][0]:
                if CardRankNumbers[game['HoleCards'][player][0][0]] > \
                    CardRankNumbers[game['HoleCards'][player][1][0]]:
                    nonPair = game['HoleCards'][player][1][0] + \
                    game['HoleCards'][player][0][0] + 'NS'
                else:
                    nonPair = game['HoleCards'][player][0][0] + \
                    game['HoleCards'][player][1][0] + 'NS'                                       
                DistinctHoleHands2_Hands[nonPair] +=1                    
                if game['Winners'].__contains__(player):                    
                    if winnerCnt == 0:
                        DistinctHoleHands2_TiedWins[nonPair] +=1
                        winnerCnt +=1
                        totalTiedGames +=1
    
    return totalTiedGames
    
def putParentData():
    """
    Pass Key Probability Parameters back to Parent using JSON
    """
    parentData = {}
    parentData['total_games'] = totalNumberOfGames
    #parentData['NonTiedGames'] = NonTiedGames
    #parentData['TiedGames'] = TiedGames
    parentData['hole_hand_wins'] = DistinctHoleHands2_Wins
    parentData['hole_hand_tied_wins'] = DistinctHoleHands2_TiedWins
    parentData['hole_hand_hands'] = DistinctHoleHands2_Hands
    parentData['player_wins'] = Player_Wins
    parentData['player_hands'] = Player_Hands
    parentData['hand_type_hands'] = HandType_Hands
    parentData['hand_type_wins'] = HandType_Wins
    
    return parentData
    
###############################################################################
############## Put Data into Texas Holdem Database  ###########################
###############################################################################
    
def putParentData2(numberOfPlayers, cpuNum, parentData, save_game_data):
    
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])    
        
        cur = cnx.cursor()
        parentData = json.dumps(parentData)
        
        if save_game_data:
            nonTiedGamesData = json.dumps(NonTiedGames)
            tiedGamesData = json.dumps(TiedGames)
              
            add_gameData = ("insert into gamesim_cpu2LoopData " 
                "(run_time, num_players, cpu_num, non_tied_hands,"
                " tied_hands, parent_data, simulation_job_id) "
                "values (%s, %s, %s, %s, %s, %s, %s);")
  
            data_gameData = (run_time, numberOfPlayers, cpuNum, \
                nonTiedGamesData, tiedGamesData, parentData, sim_id)       
        else:
            add_gameData = ("insert into gamesim_cpu2LoopData " 
                "(run_time, num_players, cpu_num,"
                " parent_data, simulation_job_id) "
                "values (%s, %s, %s, %s, %s);")
  
            data_gameData = (run_time, numberOfPlayers, cpuNum, parentData, \
                sim_id)       
        cur.execute(add_gameData, data_gameData)
        
        cnx.commit()
        cnx.close()    
        
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()    
    
    return

###############################################################################
########################  Game   ##############################################
        
cpuNum = '2'

db_params = {'username':'texasholdem', 'password': 'Texasholdem123', \
    'database': 'texasholdem_db'}
    
sim_id = int(sys.argv[1])
numberOfGames, save_game_data = th_i.getSimulationParametersChild(sim_id)

db_params = {'username':'texasholdem', 'password': 'Texasholdem123', \
    'database': 'texasholdem_db'}
    
th_i.set_global_sql_variables()

Players, Player_Wins, Player_Hands = th_i.get_game_players()

CardSuits, CardRanks, CardRankNumbers = th_i.get_cards()
HandTypes, HandType_Ranks = th_i.get_hands()
HandType_Wins, HandType_Hands = th_i.get_hand_counters()

DistinctHoleHands = th_i.get_hole_hands()
    
DistinctHoleHands2_Wins, DistinctHoleHands2_Hands, \
    DistinctHoleHands2_TiedWins = th_i.get_hole_hand_counters()

run_time = th_i.get_running_job()

numberOfTieGames, numberOfNonTieGames, totalNumberOfGames, NonTiedGames, \
    TiedGames = th_i.getGameParameters()

numberOfPlayers = len(Players)

for game in range(numberOfGames):

    PlayerCards, CardsNotAvailableToEachPlayer, HoleCards, FlopCards,\
        RiverCard, TurnCard = th_i.getInitialCardLists(Players)
    
    Game = {}
    Game['Players'] = Players

###############################################################################
####################### Shuffle the Deck, Burn the First Card, ################
####################### Deal the Hole Cards to Players ########################
    
    Deck = th_i.getShuffledDeck(CardSuits, CardRanks)

    Game['BurnCard'] = Deck[0]
    Deck.__delitem__(0)

    cardCount = 1
    cardCount = th_i.getHoleCards(cardCount, Players, HoleCards, PlayerCards, \
        Deck)
        
    Game['HoleCards'] = HoleCards

###############################################################################
################# Deal the Flop ###############################################
    cardCount = th_i.getFlopCards(cardCount, FlopCards, Players, PlayerCards, \
        Deck)
    
    Game['FlopCards'] = FlopCards
    
###############################################################################    
####################### Deal the Turn #########################################
    cardCount = th_i.getTurnCard(cardCount, TurnCard, Players, PlayerCards, \
        Deck)
 
    Game['TurnCard'] = TurnCard

###############################################################################    
####################### Deal the River #########################################
    cardCount = th_i.getRiverCard(cardCount, RiverCard, Players, PlayerCards, \
        Deck )

    Game['RiverCard'] = RiverCard
    
    for player in Players:
        PlayerCards[player]=tuple(PlayerCards[player])

###############################################################################
########################## Determine Winner ###################################

    BestHands = {}            
    for player in Players:
        BestHand = bh.DeterminePossibleHands(player, PlayerCards[player],
            CardRankNumbers, CardRanks)
        BestHands[player] = BestHand

    Game = win.DetermineWinner(Game, Players, BestHands)
    
###############################################################################
########## Increment Player, HandType, and Game Dictionaries
###############################################################################    
    
    
    numberOfTieGames, numberOfNonTieGames, totalNumberOfGames = \
        putPlayerWinsAndGameDictionaries(numberOfTieGames, \
        numberOfNonTieGames, totalNumberOfGames)
        
    putHandTypeWins()
    putHandTypeHands()

###############################################################################
########### Using Game Dictionaries Increment HoleHand Dictionaries  ##########
###############################################################################        
            
putNonTiedHoleHandWinDictionaries()                
totalTiedGames = putTiedHoleHandWinDictionaries()                

totalNumberOfGames = len(NonTiedGames) + totalTiedGames

###############################################################################
######### Return Dictionaries to parent #######################################

parentData = putParentData()

###############################################################################
################# Put Tied and NonTied Games into MYSQL Database ##############

putParentData2(numberOfPlayers, cpuNum, parentData, save_game_data)    


    





