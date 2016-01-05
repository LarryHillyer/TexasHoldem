# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:58:07 2015

@author: Larry
"""
import numpy as np
###############################################################################
#######  Functions Required to Determine Winner  ##############################
###############################################################################
            
def putBestHandType(BestHandRank, Game):
    
    if BestHandRank == 1:
        Game['BestHandType'] = 'HighCard'
    elif BestHandRank == 2:
        Game['BestHandType'] = 'OnePair'
    elif BestHandRank == 3:
        Game['BestHandType'] = 'TwoPairs'
    elif BestHandRank == 4:
        Game['BestHandType'] = 'ThreeOfAKind'
    elif BestHandRank == 5:
        Game['BestHandType'] = 'Straight'
    elif BestHandRank == 6:
        Game['BestHandType'] = 'Flush'
    elif BestHandRank == 7:
        Game['BestHandType'] = 'FullHouse'
    elif BestHandRank == 8:
        Game['BestHandType'] = 'FourOfAKind'
    elif BestHandRank == 9:
        Game['BestHandType'] = 'StraightFlush'
    
    return Game
    
def getPlayersWithBestHand(BestHandRank, BestHands, Players):
    
    PlayersWithBestHand = []
    for player in Players:
        if BestHandRank == BestHands[player][0]['HandRank']:
            PlayersWithBestHand.append(player)
    
    return PlayersWithBestHand
    
def getParameter(PlayersWithBest, parameter, BestHands, i = -1):
    
    if i == -1 :
        parameterRanks = [BestHands[player][0][parameter] for player in \
            PlayersWithBest]
    else: 
        parameterRanks = [BestHands[player][0][parameter][i] for player in \
            PlayersWithBest]
    bestParameter = np.max(parameterRanks)
    
    return bestParameter
    
def getPlayersWithParameter(PlayersWithParameter, bestParameter, parameter, \
    BestHands, i = -1):
    
    if i == -1:
        PlayersWithParameter = [player for player in PlayersWithParameter \
            if bestParameter == BestHands[player][0][parameter]]
    else:   
        PlayersWithParameter = [player for player in PlayersWithParameter \
            if bestParameter == BestHands[player][0][parameter][i]]    
    
    return PlayersWithParameter
    
def getPlayersWithBestParameter(PlayersWithParameter, parameter, BestHands,\
     i = -1):
        
    if i == -1:
        bestParameter = getParameter(PlayersWithParameter, parameter, \
            BestHands)
        return getPlayersWithParameter(PlayersWithParameter, bestParameter, \
            parameter, BestHands)
    else:
        bestParameter = getParameter(PlayersWithParameter, parameter, \
            BestHands, i)                
        return getPlayersWithParameter(PlayersWithParameter, bestParameter, \
            parameter, BestHands, i)
    
def getGameWinners(PlayerWithBestParameter, Game):
        Game['Winners'] = PlayerWithBestParameter   
        return Game

def getHighCardWinners(PlayersWithBestHand, Game, BestHands):
    PlayersWithBestKicker = getPlayersWithBestParameter(\
        PlayersWithBestHand, 'Kickers', BestHands, 0)
            
    if len(PlayersWithBestKicker) == 1:
        return getGameWinners(PlayersWithBestKicker, Game)
    else:                
        PlayersWithBestSecondKicker = getPlayersWithBestParameter(\
            PlayersWithBestKicker, 'Kickers', BestHands, 1)
                              
        if len(PlayersWithBestSecondKicker) == 1:
            return getGameWinners(PlayersWithBestSecondKicker, Game)
        else:                  
            PlayersWithBestThirdKicker = getPlayersWithBestParameter(\
                PlayersWithBestSecondKicker, 'Kickers', BestHands, 2)
                                    
            if len(PlayersWithBestThirdKicker) == 1:
                return getGameWinners(PlayersWithBestThirdKicker, Game)
            else:                        
                PlayersWithBestFourthKicker = getPlayersWithBestParameter\
                    (PlayersWithBestThirdKicker, 'Kickers', BestHands, 3)
                                                
                if len(PlayersWithBestFourthKicker) == 1:
                    return getGameWinners(PlayersWithBestFourthKicker, Game)
                else:
                    PlayersWithBestFifthKicker = getPlayersWithBestParameter\
                        (PlayersWithBestFourthKicker, 'Kickers', BestHands, 4)
                                                        
                    return getGameWinners(PlayersWithBestFifthKicker, Game) 
    return Game

def getOnePairWinners(PlayersWithBestHand, Game, BestHands):
    PlayersWithBestPair = getPlayersWithBestParameter(\
        PlayersWithBestHand, 'MatchedRanks', BestHands, 0)
            
    if len(PlayersWithBestPair) == 1:
        return getGameWinners(PlayersWithBestPair, Game)
    else:
        PlayersWithBestKicker = getPlayersWithBestParameter(\
            PlayersWithBestPair, 'Kickers', BestHands, 0)
                                
        if len(PlayersWithBestKicker) == 1:
            return getGameWinners(PlayersWithBestKicker, Game)
        else:
            PlayersWithBestSecondKicker = getPlayersWithBestParameter(\
                PlayersWithBestKicker, 'Kickers', BestHands, 1)
                                        
            if len(PlayersWithBestSecondKicker) == 1:
                return getGameWinners(PlayersWithBestSecondKicker, Game)
            else:
                PlayersWithBestThirdKicker = getPlayersWithBestParameter(\
                    PlayersWithBestSecondKicker, 'Kickers', BestHands, 2)
                                                
                return getGameWinners(PlayersWithBestThirdKicker, Game) 
    return Game
    
def getTwoPairsWinners(PlayersWithBestHand, Game, BestHands):
    PlayersWithBestPair = getPlayersWithBestParameter(\
        PlayersWithBestHand, 'MatchedRanks', BestHands, 0)
                            
    if len(PlayersWithBestPair) == 1:
        return getGameWinners(PlayersWithBestPair, Game)
    else:                
        PlayersWithBestSecondPair = getPlayersWithBestParameter(\
            PlayersWithBestPair, 'MatchedRanks', BestHands, 1)
                                
        if len(PlayersWithBestSecondPair) == 1:
            return getGameWinners(PlayersWithBestSecondPair, Game)
        else:
            PlayersWithBestKicker = getPlayersWithBestParameter(\
                PlayersWithBestSecondPair, 'Kickers', BestHands, 0)
                                        
            return getGameWinners(PlayersWithBestKicker, Game)   
    return Game
    
def getThreeOfAKindWinners(PlayersWithBestHand, Game, BestHands):
    PlayersWithBestThreeOfAKind = getPlayersWithBestParameter(\
        PlayersWithBestHand, 'MatchedRanks',  BestHands, 0)
                        
    if len(PlayersWithBestThreeOfAKind) == 1:
        return getGameWinners(PlayersWithBestThreeOfAKind, Game)
    else:
        PlayersWithBestKicker = getPlayersWithBestParameter(\
            PlayersWithBestThreeOfAKind, 'Kickers', BestHands, 0)
                
        if len(PlayersWithBestKicker) == 1:
            return getGameWinners(PlayersWithBestKicker, Game)
        else:
            PlayersWithBestSecondKicker = getPlayersWithBestParameter(\
                PlayersWithBestKicker, 'Kickers', BestHands, 1)
                                            
            return getGameWinners(PlayersWithBestSecondKicker, Game)   
    return Game
    
def getStraightWinners(PlayersWithBestHand, Game, BestHands):
    PlayersWithBestStraight = getPlayersWithBestParameter(\
        PlayersWithBestHand, 'HighCardRank', BestHands)

    return getGameWinners(PlayersWithBestStraight, Game)
    
def getFlushWinners(PlayersWithBestHand,  Game, BestHands):
    PlayersWithBestFlush = getPlayersWithBestParameter(\
        PlayersWithBestHand, 'HighCardRank', BestHands)
            
    return getGameWinners(PlayersWithBestFlush, Game)
    
def getFullHouseWinners(PlayersWithBestHand, Game, BestHands):
    PlayersWithBestFullHouse = getPlayersWithBestParameter(\
        PlayersWithBestHand, 'MatchedRanks', BestHands, 0)
                        
    if len(PlayersWithBestFullHouse) == 1:
        return getGameWinners(PlayersWithBestFullHouse, Game)
    else:
        PlayersWithBestPair = getPlayersWithBestParameter(\
            PlayersWithBestFullHouse, 'MatchedRanks', BestHands, 1)
                
        return getGameWinners(PlayersWithBestPair, Game)
        
def getFourOfAKindWinners(PlayersWithBestHand, Game, BestHands):
    PlayersWithBestFourOfAKind = getPlayersWithBestParameter(\
        PlayersWithBestHand, 'MatchedRanks', BestHands, 0)
            
    if len(PlayersWithBestFourOfAKind) == 1:
        return getGameWinners(PlayersWithBestFourOfAKind, Game)
    else:
        PlayersWithBestKicker = getPlayersWithBestParameter(\
            PlayersWithBestFourOfAKind, 'Kickers', BestHands, 0)
                
    return getGameWinners(PlayersWithBestKicker, Game)
    
def getStraightFlushWinners(PlayersWithBestHand, Game, BestHands):    
    PlayersWithBestStraightFlush = getPlayersWithBestParameter(\
        PlayersWithBestHand, 'HighCardRank', BestHands)
            
    return getGameWinners(PlayersWithBestStraightFlush, Game)
       
def getWinners(BestHandRank, PlayersWithBestHand, Game, BestHands):
    
    if len(PlayersWithBestHand) == 1:        
        return getGameWinners(PlayersWithBestHand, Game)
    else:
        if BestHandRank == 1:
            return getHighCardWinners(PlayersWithBestHand, Game, BestHands)                                                
        elif BestHandRank == 2:
            return getOnePairWinners(PlayersWithBestHand, Game, BestHands)                                                                                    
        elif BestHandRank == 3:
            return getTwoPairsWinners(PlayersWithBestHand, Game, BestHands)                                                                                                                    
        elif BestHandRank == 4:
            return getThreeOfAKindWinners(PlayersWithBestHand, Game, BestHands)                                                                                                                                           
        elif BestHandRank == 5:
            return getStraightWinners(PlayersWithBestHand, Game, BestHands)                                                                                                                                                                   
        elif BestHandRank == 6:
            return getFlushWinners(PlayersWithBestHand, Game, BestHands)                                                                                                                                                       
        elif BestHandRank == 7:
            return getFullHouseWinners(PlayersWithBestHand, Game, BestHands)                   
        elif BestHandRank == 8:
            return getFourOfAKindWinners(PlayersWithBestHand, Game, BestHands)                   
        elif BestHandRank == 9:
            return getStraightFlushWinners(PlayersWithBestHand, Game, BestHands)                   
                      
def DetermineWinner(Game, Players, BestHands):

    HandRanks = [BestHands[player][0]['HandRank'] for player in Players ]
    BestHandRank = np.max(HandRanks)
    
    Game = putBestHandType(BestHandRank, Game)

    PlayersWithBestHand = getPlayersWithBestHand(BestHandRank, BestHands, \
        Players)    
    
    Game = getWinners(BestHandRank, PlayersWithBestHand, Game, BestHands)        

    return Game
    
