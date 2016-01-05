# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:57:34 2015

@author: Larry
"""

###############################################################################
##################### Function Required to Generate Player Hands #########################
###############################################################################
def makePlayerHands(PlayerCards):
    
    #Indexes of cards not included in hand
    ExcludedCardIndexes = ((0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,2),(1,3),\
        (1,4),(1,5),(1,6),(2,3),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6),(4,5),\
        (4,6),(5,6))
    
    PlayerHands = []
    for i in range(len(ExcludedCardIndexes)):
        PlayerHands.append([])
    for cnt, eCI in enumerate(ExcludedCardIndexes):    
        for i, card in enumerate(PlayerCards):               
            if i != eCI[0] and i != eCI[1]:
                if not (PlayerHands[cnt].__contains__(card)):
                    PlayerHands[cnt].append(card)
    
    return PlayerHands

###############################################################################
###########Functions called by the DetermineMatches function  #################
###############################################################################
    
def seperateMatchAndUnmatchedCards(cnt, playerHand, UnmatchedCards_InHands, \
    PossibleHandTotals_Rank, CardRankNumbers, CardRanks):

    CardRankNumbers2 = {2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'T',\
                        11:'J',12:'Q',13:'K',14:'A'}
        
    UnmatchedCards_InHand = []
    UnmatchedCardNumbers_Hand = []
    UnmatchedCards = []
        
    MatchedRanks = []
    MatchedRankTotals = {}
    
    for rank in CardRanks:
        if PossibleHandTotals_Rank[cnt][rank] > 1:
            MatchedRanks.append(rank)
            MatchedRankTotals[rank]=PossibleHandTotals_Rank[cnt][rank]
        elif PossibleHandTotals_Rank[cnt][rank] == 1:
            for card in playerHand:
                if card[0] == rank:
                    UnmatchedCards_InHand.append(card)
                    UnmatchedCardNumbers_Hand.append(CardRankNumbers[card[0]])
            UnmatchedCardNumbers_Hand.sort()
            UnmatchedCardNumbers_Hand.reverse()                
            for rankNumber in UnmatchedCardNumbers_Hand:
                for card in UnmatchedCards_InHand:
                    if card[0] == CardRankNumbers2[rankNumber]:
                        UnmatchedCards.append(card)
                        UnmatchedCards_InHand.remove(card)
                        break
            UnmatchedCards.reverse()
            UnmatchedCards_InHands.append(UnmatchedCards)

    return UnmatchedCards_InHand, UnmatchedCardNumbers_Hand, UnmatchedCards,\
        UnmatchedCards_InHands, MatchedRanks, MatchedRankTotals

class MatchedRankSorter(object):
    def __init__(self, matchRank1):
        self.found1 = False
        self.found2 = False
        self.matchRank1 = matchRank1[0]
        if len(matchRank1) == 2:
            self.matchRank2 = matchRank1[1]
        else:
            self.matchRank2 = ''
    
    def __call__(self, card):
        if card[0] in self.matchRank1:
            self.found1 = True
            return (0, card)
        elif self.matchRank2 != '':
            if card[0] in self.matchRank2:
                self.found2 = True
                return (1,card)
        return (2, card)

def sortMatchedRankNumbers(MatchedRanks, CardRankNumbers):
    
    sortedMatchedRankNumbers = [CardRankNumbers[rank] for rank in\
        MatchedRanks]
                
    sortedMatchedRankNumbers.sort()
    sortedMatchedRankNumbers.reverse()
    
    return sortedMatchedRankNumbers
    
def putHighCardInfo(FourOfAKindInfos,  FullHouseInfos, ThreeOfAKindInfos, \
    TwoPairsInfos, OnePairInfos, HighCardInfos, UnmatchedCards, \
    UnmatchedCardNumbers_Hand):

    FourOfAKindInfo = {}
    FullHouseInfo = {}
    ThreeOfAKindInfo = {}
    TwoPairsInfo = {}
    OnePairInfo = {}
    HighCardInfo = {}
      
    FourOfAKindInfo['IsPresent']='false'
    FullHouseInfo['IsPresent']='false'
    ThreeOfAKindInfo['IsPresent']='false'
    TwoPairsInfo['IsPresent']='false'
    OnePairInfo['IsPresent']='false'
             
    HighCardInfo['IsPresent'] = 'true'
    HighCardInfo['Hand'] = tuple(UnmatchedCards)
    HighCardInfo['HandRank'] = 1
    HighCardInfo['HandType'] = 'HighCard'
    HighCardInfo['Kickers'] = tuple(UnmatchedCardNumbers_Hand)
            
    FourOfAKindInfos.append(FourOfAKindInfo)
    FullHouseInfos.append(FullHouseInfo)
    ThreeOfAKindInfos.append(ThreeOfAKindInfo)
    TwoPairsInfos.append(TwoPairsInfo)
    OnePairInfos.append(OnePairInfo)
    HighCardInfos.append(HighCardInfo)
    
    
    return FourOfAKindInfo, FourOfAKindInfos, FullHouseInfo, FullHouseInfos,\
        ThreeOfAKindInfo, ThreeOfAKindInfos, TwoPairsInfo, TwoPairsInfos,\
        OnePairInfo, OnePairInfos, HighCardInfo, HighCardInfos
    
def putFourOfAKindInfo(FourOfAKindInfos,  FullHouseInfos, ThreeOfAKindInfos, \
    TwoPairsInfos, OnePairInfos, HighCardInfos, UnmatchedCards, \
    UnmatchedCardNumbers_Hand, MatchedRanks, playerHand, CardRankNumbers):

    FourOfAKindInfo = {}
    FullHouseInfo = {}
    ThreeOfAKindInfo = {}
    TwoPairsInfo = {}
    OnePairInfo = {}
    HighCardInfo = {}
      
    FourOfAKindInfo['IsPresent']='true'
    FourOfAKindInfo['Hand']=tuple(playerHand)
    FourOfAKindInfo['HandRank'] = 8
    FourOfAKindInfo['HandType'] = 'FourOfAKind'                
    FourOfAKindInfo['MatchedRanks']=tuple([CardRankNumbers[MatchedRanks[0]]])
    FourOfAKindInfo['Kickers']=tuple(UnmatchedCardNumbers_Hand)
                        
    FullHouseInfo['IsPresent']='false'
    ThreeOfAKindInfo['IsPresent']='false'
    TwoPairsInfo['IsPresent']='false'
    OnePairInfo['IsPresent']='false'
    HighCardInfo['IsPresent']='false'
                
    FourOfAKindInfos.append(FourOfAKindInfo)
    FullHouseInfos.append(FullHouseInfo)
    ThreeOfAKindInfos.append(ThreeOfAKindInfo)
    TwoPairsInfos.append(TwoPairsInfo)
    OnePairInfos.append(OnePairInfo)
    HighCardInfos.append(HighCardInfo)
    
    
    return FourOfAKindInfo, FourOfAKindInfos, FullHouseInfo, FullHouseInfos,\
        ThreeOfAKindInfo, ThreeOfAKindInfos, TwoPairsInfo, TwoPairsInfos,\
        OnePairInfo, OnePairInfos, HighCardInfo, HighCardInfos
    
def putThreeOfAKindInfo(FourOfAKindInfos,  FullHouseInfos, ThreeOfAKindInfos, \
    TwoPairsInfos, OnePairInfos, HighCardInfos, UnmatchedCards, \
    UnmatchedCardNumbers_Hand, MatchedRanks, playerHand, CardRankNumbers):

    FourOfAKindInfo = {}
    FullHouseInfo = {}
    ThreeOfAKindInfo = {}
    TwoPairsInfo = {}
    OnePairInfo = {}
    HighCardInfo = {}
      
    FourOfAKindInfo['IsPresent']='false'
    FullHouseInfo['IsPresent']='false'
                    
    ThreeOfAKindInfo['IsPresent']='true'
    ThreeOfAKindInfo['Hand']=tuple(playerHand)
    ThreeOfAKindInfo['HandRank'] = 4
    ThreeOfAKindInfo['HandType'] = 'ThreeOfAKind'                
    ThreeOfAKindInfo['MatchedRanks']=tuple([CardRankNumbers[MatchedRanks[0]]])                
    ThreeOfAKindInfo['Kickers']=tuple(UnmatchedCardNumbers_Hand)

    TwoPairsInfo['IsPresent']='false'
    OnePairInfo['IsPresent']='false'
    HighCardInfo['IsPresent']='false'
                
    FourOfAKindInfos.append(FourOfAKindInfo)
    FullHouseInfos.append(FullHouseInfo)
    ThreeOfAKindInfos.append(ThreeOfAKindInfo)
    TwoPairsInfos.append(TwoPairsInfo)
    OnePairInfos.append(OnePairInfo)
    HighCardInfos.append(HighCardInfo)
    
    
    return FourOfAKindInfo, FourOfAKindInfos, FullHouseInfo, FullHouseInfos,\
        ThreeOfAKindInfo, ThreeOfAKindInfos, TwoPairsInfo, TwoPairsInfos,\
        OnePairInfo, OnePairInfos, HighCardInfo, HighCardInfos
    
def putOnePairInfo(FourOfAKindInfos,  FullHouseInfos, ThreeOfAKindInfos, \
    TwoPairsInfos, OnePairInfos, HighCardInfos, UnmatchedCards, \
    UnmatchedCardNumbers_Hand, MatchedRanks, playerHand, CardRankNumbers):

    FourOfAKindInfo = {}
    FullHouseInfo = {}
    ThreeOfAKindInfo = {}
    TwoPairsInfo = {}
    OnePairInfo = {}
    HighCardInfo = {}
      
    FourOfAKindInfo['IsPresent']='false'
    FullHouseInfo['IsPresent']='false'
    ThreeOfAKindInfo['IsPresent']='false'
    TwoPairsInfo['IsPresent']='false'
                    
    OnePairInfo['IsPresent']='true'
    OnePairInfo['Hand']=tuple(playerHand)
    OnePairInfo['HandRank'] = 2
    OnePairInfo['HandType'] = 'OnePair'                
    OnePairInfo['MatchedRanks']=tuple([CardRankNumbers[MatchedRanks[0]]])                
    OnePairInfo['Kickers']=tuple(UnmatchedCardNumbers_Hand)
                
    HighCardInfo['IsPresent']='false'
                
    FourOfAKindInfos.append(FourOfAKindInfo)
    FullHouseInfos.append(FullHouseInfo)
    ThreeOfAKindInfos.append(ThreeOfAKindInfo)
    TwoPairsInfos.append(TwoPairsInfo)
    OnePairInfos.append(OnePairInfo)
    HighCardInfos.append(HighCardInfo)                
       
    return FourOfAKindInfo, FourOfAKindInfos, FullHouseInfo, FullHouseInfos,\
        ThreeOfAKindInfo, ThreeOfAKindInfos, TwoPairsInfo, TwoPairsInfos,\
        OnePairInfo, OnePairInfos, HighCardInfo, HighCardInfos

def putFullHouseInfo(FourOfAKindInfos,  FullHouseInfos, ThreeOfAKindInfos, \
    TwoPairsInfos, OnePairInfos, HighCardInfos, UnmatchedCards, \
    UnmatchedCardNumbers_Hand, MatchedRanks, playerHand, \
    ThreeOfAKindRankNumbers):

    FourOfAKindInfo = {}
    FullHouseInfo = {}
    ThreeOfAKindInfo = {}
    TwoPairsInfo = {}
    OnePairInfo = {}
    HighCardInfo = {}
      
    FourOfAKindInfo['IsPresent']='false'
                               
    FullHouseInfo['IsPresent']='true'
    FullHouseInfo['Hand']=tuple(playerHand)
    FullHouseInfo['HandRank'] = 7
    FullHouseInfo['HandType'] = 'FullHouse'                                  
    FullHouseInfo['MatchedRanks']=tuple(ThreeOfAKindRankNumbers)
                                      
    ThreeOfAKindInfo['IsPresent']='false'
    TwoPairsInfo['IsPresent']='false'
    OnePairInfo['IsPresent']='false'
    HighCardInfo['IsPresent']='false'
                   
    FourOfAKindInfos.append(FourOfAKindInfo)
    FullHouseInfos.append(FullHouseInfo)
    ThreeOfAKindInfos.append(ThreeOfAKindInfo)
    TwoPairsInfos.append(TwoPairsInfo)
    OnePairInfos.append(OnePairInfo)
    HighCardInfos.append(HighCardInfo)
       
    return FourOfAKindInfo, FourOfAKindInfos, FullHouseInfo, FullHouseInfos,\
        ThreeOfAKindInfo, ThreeOfAKindInfos, TwoPairsInfo, TwoPairsInfos,\
        OnePairInfo, OnePairInfos, HighCardInfo, HighCardInfos

def putTwoPairsInfo(FourOfAKindInfos,  FullHouseInfos, ThreeOfAKindInfos, \
    TwoPairsInfos, OnePairInfos, HighCardInfos, UnmatchedCards, \
    UnmatchedCardNumbers_Hand, MatchedRanks, playerHand, \
    TwoPairsRankNumbers):

    FourOfAKindInfo = {}
    FullHouseInfo = {}
    ThreeOfAKindInfo = {}
    TwoPairsInfo = {}
    OnePairInfo = {}
    HighCardInfo = {}
      
    FourOfAKindInfo['IsPresent']='false'
    FullHouseInfo['IsPresent']='false'
    ThreeOfAKindInfo['IsPresent']='false'

    TwoPairsInfo['IsPresent']='true'
    TwoPairsInfo['Hand']=tuple(playerHand)
    TwoPairsInfo['HandRank'] = 3
    TwoPairsInfo['HandType'] = 'TwoPairs'                                
    TwoPairsInfo['MatchedRanks']=tuple(TwoPairsRankNumbers)
    TwoPairsInfo['Kickers']=tuple(UnmatchedCardNumbers_Hand)

    OnePairInfo['IsPresent']='false'
    HighCardInfo['IsPresent']='false'

    FourOfAKindInfos.append(FourOfAKindInfo)
    FullHouseInfos.append(FullHouseInfo)
    ThreeOfAKindInfos.append(ThreeOfAKindInfo)
    TwoPairsInfos.append(TwoPairsInfo)
    OnePairInfos.append(OnePairInfo)
    HighCardInfos.append(HighCardInfo)
       
    return FourOfAKindInfo, FourOfAKindInfos, FullHouseInfo, FullHouseInfos,\
        ThreeOfAKindInfo, ThreeOfAKindInfos, TwoPairsInfo, TwoPairsInfos,\
        OnePairInfo, OnePairInfos, HighCardInfo, HighCardInfos
    
def getBestFourOfAKindHand(FourOfAKindInfo, FourOfAKindInfos):
    
    if len(FourOfAKindInfos) == 1:        
        for hand in FourOfAKindInfos:
            if hand['IsPresent'] == 'true':
                FourOfAKindInfo = hand
    elif len(FourOfAKindInfos) > 1:
        highKicker = 0
        for hand in FourOfAKindInfos:
            if hand['IsPresent'] == 'true':
                if hand['Kickers'][0] > highKicker:
                    highKicker = hand['Kickers'][0]
                    FourOfAKindInfo = hand
    
    return FourOfAKindInfo

def getBestFullHouseHand(FullHouseInfo, FullHouseInfos):
    if len(FullHouseInfos) == 1:        
        for hand in FullHouseInfos:
            if hand['IsPresent'] == 'true':
                FullHouseInfo = hand
    elif len(FullHouseInfos) > 1:
        MaxThreeOfAKindRank = 0
        HighMatchFullHouseInfos = []
        for hand in FullHouseInfos:
            if hand['IsPresent'] == 'true':
                if hand['MatchedRanks'][0] >= MaxThreeOfAKindRank:
                    MaxThreeOfAKindRank = hand['MatchedRanks'][0]
        for hand in FullHouseInfos:
            if hand['IsPresent'] == 'true':
                if hand['MatchedRanks'][0] == MaxThreeOfAKindRank:
                    HighMatchFullHouseInfos.append(hand)
        MaxPairRank = 0
        for hand in HighMatchFullHouseInfos:
            MaxPairRank = 0
            if hand['MatchedRanks'][1] == MaxPairRank:
                MaxPairRank = hand['MatchedRanks'][1]
                FullHouseInfo = hand    
    return FullHouseInfo
    
def getBestThreeOfAKindHand(ThreeOfAKindInfo, ThreeOfAKindInfos):
    
    if len(ThreeOfAKindInfos) == 1:        
        for hand in ThreeOfAKindInfos:
            if hand['IsPresent'] == 'true':
                ThreeOfAKindInfo = hand
    elif len(ThreeOfAKindInfos) > 1:
        maxKicker = 0
        ThreeOfAKindMaxKickerInfos = []
        for hand in ThreeOfAKindInfos:
            if hand['IsPresent'] == 'true':
                if hand['Kickers'][0] > maxKicker:
                    maxKicker = hand['Kickers'][0]
        for hand in ThreeOfAKindInfos:
            if hand['IsPresent'] == 'true':
                if hand['Kickers'][0] == maxKicker:
                    ThreeOfAKindMaxKickerInfos.append(hand)
        secondKicker = 0
        for hand in ThreeOfAKindMaxKickerInfos:
            if hand['Kickers'][1] >= secondKicker:
                secondKicker = hand['Kickers'][1]
                ThreeOfAKindInfo = hand
    
    return ThreeOfAKindInfo
    
def getBestTwoPairsHand(TwoPairsInfo, TwoPairsInfos):
    
    if len(TwoPairsInfos) == 1:        
        for hand in TwoPairsInfos:
            if hand['IsPresent'] == 'true':
                TwoPairsInfo = hand
    elif len(TwoPairsInfos) > 1:
        MaxPairRank = 0
        HighMatchTwoPairsInfos = []
        for hand in TwoPairsInfos:
            if hand['IsPresent'] == 'true':
                if hand['MatchedRanks'][0] >= MaxPairRank:
                    MaxPairRank = hand['MatchedRanks'][0]
        for hand in TwoPairsInfos:
            if hand['IsPresent'] == 'true':                    
                if hand['MatchedRanks'][0] == MaxPairRank:
                    HighMatchTwoPairsInfos.append(hand)                    
        MaxSecondPairRank = 0
        HighMatchTwoPairsSecondPairInfos = []
        for hand in HighMatchTwoPairsInfos:
            MaxSecondPairRank = 0
            if hand['MatchedRanks'][1] == MaxSecondPairRank:
                MaxSecondPairRank = hand['MatchedRanks'][1]
        for hand in HighMatchTwoPairsInfos:
            if hand['MatchedRanks'][1] == MaxSecondPairRank:            
                HighMatchTwoPairsSecondPairInfos.append(hand)                                
        maxKicker = 0
        for hand in HighMatchTwoPairsSecondPairInfos:
            if hand['Kickers'] > maxKicker:
                maxKicker = hand['Kickers']          
                TwoPairsInfo = hand
    
    return TwoPairsInfo
    
def getBestOnePairHand(OnePairInfo, OnePairInfos):
    
    if len(OnePairInfos) == 1:        
        for hand in OnePairInfos:
            if hand['IsPresent'] == 'true':
                OnePairInfo = hand
    elif len(OnePairInfos) > 1:
        maxKicker = 0
        OnePairMaxKickerInfos = []
        for hand in OnePairInfos:
            if hand['IsPresent'] == 'true':
                if hand['Kickers'][0] > maxKicker:
                    maxKicker = hand['Kickers'][0]
        for hand in OnePairInfos:
            if hand['IsPresent'] == 'true':
                if hand['Kickers'][0] == maxKicker:
                    OnePairMaxKickerInfos.append(hand)
        secondKicker = 0
        OnePairSecondKickerInfos = []
        for hand in OnePairMaxKickerInfos:
            if hand['Kickers'][1] >= secondKicker:
                secondKicker = hand['Kickers'][1]
        for hand in OnePairMaxKickerInfos:
            if hand['Kickers'][1] == secondKicker:
                OnePairSecondKickerInfos.append(hand)
        thirdKicker = 0
        for hand in OnePairSecondKickerInfos:
            if hand['Kickers'][2] >= thirdKicker:
                thirdKicker = hand['Kickers'][2]
                OnePairInfo = hand
    
    return OnePairInfo
    
def getBestHighCardHand(HighCardInfo, HighCardInfos):
    if len(HighCardInfos) == 1:        
        for hand in HighCardInfos:
            if hand['IsPresent'] == 'true':
                HighCardInfo = hand
    elif len(HighCardInfos) > 1:
        maxKicker = 0
        HighCardMaxKickerInfos = []
        for hand in HighCardInfos:
            if hand['IsPresent'] == 'true':
                if hand['Kickers'][0] > maxKicker:
                    maxKicker = hand['Kickers'][0]
        for hand in HighCardInfos:
            if hand['IsPresent'] == 'true':
                if hand['Kickers'][0] == maxKicker:
                    HighCardMaxKickerInfos.append(hand)
        secondKicker = 0
        HighCardSecondKickerInfos = []
        for hand in HighCardMaxKickerInfos:
            if hand['Kickers'][1] >= secondKicker:
                secondKicker = hand['Kickers'][1]
        for hand in HighCardMaxKickerInfos:
            if hand['Kickers'][1] == secondKicker:
                HighCardSecondKickerInfos.append(hand)
        thirdKicker = 0
        HighCardThirdKickerInfos = []        
        for hand in HighCardSecondKickerInfos:
            if hand['Kickers'][2] >= thirdKicker:
                thirdKicker = hand['Kickers'][2]
        for hand in HighCardSecondKickerInfos:
            if hand['Kickers'][2] == thirdKicker:
                HighCardThirdKickerInfos.append(hand)
        fourthKicker = 0
        HighCardFourthKickerInfos = []        
        for hand in HighCardThirdKickerInfos:
            if hand['Kickers'][3] >= fourthKicker:
                fourthKicker = hand['Kickers'][3]
        for hand in HighCardThirdKickerInfos:
            if hand['Kickers'][3] == fourthKicker:
                HighCardFourthKickerInfos.append(hand)
        fifthKicker = 0
        for hand in HighCardFourthKickerInfos:
            if hand['Kickers'][4] >= fifthKicker:
                fifthKicker = hand['Kickers'][4]       
                HighCardInfo = hand
    
    return HighCardInfo
    
###############################################################################
########## Function which Determine what Kind and how many matches are in a ###
##########################   Hand  ############################################
    
def DetermineMatches(player, PlayerHands,PossibleHandTotals_Rank, \
    PossibleHandTotals_Suit, CardRankNumbers, CardRanks):
                         
    FourOfAKindInfos = []
    FullHouseInfos = []
    ThreeOfAKindInfos = []
    TwoPairsInfos = []
    OnePairInfos = []
    HighCardInfos = []
        
    UnmatchedCards_InHands = []
    
    for cnt, playerHand in enumerate(PlayerHands):
        
        UnmatchedCards_InHand, UnmatchedCardNumbers_Hand, UnmatchedCards,\
            UnmatchedCards_InHands, MatchedRanks, MatchedRankTotals = \
            seperateMatchAndUnmatchedCards(cnt, playerHand, \
            UnmatchedCards_InHands, PossibleHandTotals_Rank, \
            CardRankNumbers, CardRanks)
        
        FourOfAKindInfo = {}
        FullHouseInfo = {}
        ThreeOfAKindInfo = {}
        TwoPairsInfo = {}
        OnePairInfo = {}
        HighCardInfo = {}
         
        if len(MatchedRanks) == 0:
            
            FourOfAKindInfo, FourOfAKindInfos, FullHouseInfo, FullHouseInfos,\
                ThreeOfAKindInfo,ThreeOfAKindInfos, TwoPairsInfo, \
                TwoPairsInfos, OnePairInfo, OnePairInfos, HighCardInfo,\
                HighCardInfos = putHighCardInfo(FourOfAKindInfos, \
                FullHouseInfos, ThreeOfAKindInfos, TwoPairsInfos, \
                OnePairInfos, HighCardInfos, UnmatchedCards, \
                UnmatchedCardNumbers_Hand)
            
        elif len(MatchedRanks) == 1:
            
            if MatchedRankTotals[MatchedRanks[0]] == 4:
                
                fourOfAKindSorter = MatchedRankSorter(\
                    [str(MatchedRankTotals[MatchedRanks[0]])])
                     
                playerHand.sort(key = fourOfAKindSorter)
                                
                FourOfAKindInfo, FourOfAKindInfos, FullHouseInfo, FullHouseInfos,\
                    ThreeOfAKindInfo,ThreeOfAKindInfos, TwoPairsInfo, \
                    TwoPairsInfos, OnePairInfo, OnePairInfos, HighCardInfo,\
                    HighCardInfos = putFourOfAKindInfo(FourOfAKindInfos, \
                    FullHouseInfos, ThreeOfAKindInfos, TwoPairsInfos, \
                    OnePairInfos, HighCardInfos, UnmatchedCards, \
                    UnmatchedCardNumbers_Hand, MatchedRanks, playerHand, \
                    CardRankNumbers)
                
            elif MatchedRankTotals[MatchedRanks[0]] == 3:
                
                threeOfAKindSorter = MatchedRankSorter(\
                    [str(MatchedRankTotals[MatchedRanks[0]])])
                     
                playerHand.sort(key = threeOfAKindSorter)
                
                FourOfAKindInfo, FourOfAKindInfos, FullHouseInfo, FullHouseInfos,\
                    ThreeOfAKindInfo,ThreeOfAKindInfos, TwoPairsInfo, \
                    TwoPairsInfos, OnePairInfo, OnePairInfos, HighCardInfo,\
                    HighCardInfos = putThreeOfAKindInfo(FourOfAKindInfos, \
                    FullHouseInfos, ThreeOfAKindInfos, TwoPairsInfos, \
                    OnePairInfos, HighCardInfos, UnmatchedCards, \
                    UnmatchedCardNumbers_Hand, MatchedRanks, playerHand, \
                    CardRankNumbers)
                               
            elif MatchedRankTotals[MatchedRanks[0]] == 2:
                
                onePairSorter = MatchedRankSorter(\
                    [str(MatchedRankTotals[MatchedRanks[0]])])
                     
                playerHand.sort(key = onePairSorter)
                
                FourOfAKindInfo, FourOfAKindInfos, FullHouseInfo, FullHouseInfos,\
                    ThreeOfAKindInfo,ThreeOfAKindInfos, TwoPairsInfo, \
                    TwoPairsInfos, OnePairInfo, OnePairInfos, HighCardInfo,\
                    HighCardInfos = putOnePairInfo(FourOfAKindInfos, \
                    FullHouseInfos, ThreeOfAKindInfos, TwoPairsInfos, \
                    OnePairInfos, HighCardInfos, UnmatchedCards, \
                    UnmatchedCardNumbers_Hand, MatchedRanks, playerHand, \
                    CardRankNumbers)
                           
        elif len(MatchedRanks) == 2:
            
            if MatchedRankTotals[MatchedRanks[0]] == 3 or \
               MatchedRankTotals[MatchedRanks[1]] == 3 :
                   
                fullHouseSorter = MatchedRankSorter(\
                    [str(MatchedRankTotals[MatchedRanks[0]])])
                     
                playerHand.sort(key = fullHouseSorter)
                                      
                ThreeOfAKindRankNumbers = sortMatchedRankNumbers(MatchedRanks,\
                    CardRankNumbers)

                FourOfAKindInfo, FourOfAKindInfos, FullHouseInfo, FullHouseInfos,\
                    ThreeOfAKindInfo,ThreeOfAKindInfos, TwoPairsInfo, \
                    TwoPairsInfos, OnePairInfo, OnePairInfos, HighCardInfo,\
                    HighCardInfos = putFullHouseInfo(FourOfAKindInfos, \
                    FullHouseInfos, ThreeOfAKindInfos, TwoPairsInfos, \
                    OnePairInfos, HighCardInfos, UnmatchedCards, \
                    UnmatchedCardNumbers_Hand, MatchedRanks, playerHand, \
                    ThreeOfAKindRankNumbers)                   
            else:
                
                twoPairsSorter = MatchedRankSorter(\
                    [str(MatchedRankTotals[MatchedRanks[0]]),\
                    str(MatchedRankTotals[MatchedRanks[1]])])
                     
                playerHand.sort(key = twoPairsSorter)
                
                TwoPairsRankNumbers = sortMatchedRankNumbers(MatchedRanks,\
                    CardRankNumbers)

                FourOfAKindInfo, FourOfAKindInfos, FullHouseInfo, FullHouseInfos,\
                    ThreeOfAKindInfo,ThreeOfAKindInfos, TwoPairsInfo, \
                    TwoPairsInfos, OnePairInfo, OnePairInfos, HighCardInfo,\
                    HighCardInfos = putTwoPairsInfo(FourOfAKindInfos, \
                    FullHouseInfos, ThreeOfAKindInfos, TwoPairsInfos, \
                    OnePairInfos, HighCardInfos, UnmatchedCards, \
                    UnmatchedCardNumbers_Hand, MatchedRanks, playerHand, \
                    TwoPairsRankNumbers)                   
                
    FourOfAKindInfo = getBestFourOfAKindHand(FourOfAKindInfo, FourOfAKindInfos)            
    FullHouseInfo = getBestFullHouseHand(FullHouseInfo, FullHouseInfos)            
    ThreeOfAKindInfo = getBestThreeOfAKindHand(ThreeOfAKindInfo, \
        ThreeOfAKindInfos)            
    TwoPairsInfo = getBestTwoPairsHand(TwoPairsInfo, TwoPairsInfos)            
    OnePairInfo = getBestOnePairHand(OnePairInfo, OnePairInfos)            
    HighCardInfo = getBestHighCardHand(HighCardInfo, HighCardInfos)
                
    return FourOfAKindInfo, FullHouseInfo, ThreeOfAKindInfo, TwoPairsInfo,\
            OnePairInfo, HighCardInfo
    
    
    
##############################################################################
######## Functions required by DetermineStraightFlush Function  ##############
##############################################################################    

def addStraightInfo(cnt, playerHand, highCard, highCardRank, StraightInfo, \
    StraightInfos):
    StraightInfo['IsPresent'] = 'true'
    StraightInfo['HighCard'] = highCard[0]
    StraightInfo['HighCardRank'] = highCardRank
    StraightInfo['Hand'] = playerHand
    StraightInfo['HandNumber'] = cnt
    StraightInfo['HandRank'] = 5
    StraightInfo['HandType'] = 'Straight'
    StraightInfos.append(StraightInfo)

    return StraightInfo, StraightInfos
    
def addFlushInfo(cnt, playerHand, highCard, highCardRank, FlushInfo, \
    FlushInfos):
    FlushInfo['IsPresent']='true'
    FlushInfo['Suit']=highCard[1]
    FlushInfo['HighCard']=highCard[0]
    FlushInfo['HighCardRank']=highCardRank                    
    FlushInfo['Hand']=playerHand
    FlushInfo['HandNumber']=cnt                    
    FlushInfo['HandRank']=6
    FlushInfo['HandType']='Flush'                    
    FlushInfos.append(FlushInfo)
    
    return FlushInfo, FlushInfos
        
def addStraightFlushInfo(StraightInfo, FlushInfo, cnt, playerHand,
    StraightFlushInfo, StraightFlushInfos):
    
    StraightFlushInfo['IsPresent']='true'
    StraightFlushInfo['HighCard']=StraightInfo['HighCard']
    StraightFlushInfo['HighCardRank']=StraightInfo['HighCardRank']
    StraightFlushInfo['Suit']=FlushInfo['Suit']
    StraightFlushInfo['Hand']=playerHand
    StraightFlushInfo['HandNumber'] = cnt
    StraightFlushInfo['HandRank']=9
    StraightFlushInfo['HandType']='StraightFlush'                                                 
    StraightFlushInfos.append(StraightFlushInfo)
    
    return StraightFlushInfo, StraightFlushInfos    
    
def getStraights(cnt, playerHand, highCard, highCardRank, StraightInfo,\
    StraightInfos, PossibleHandTotals_Rank):
        
    if PossibleHandTotals_Rank[cnt]['A'] > 0 and \
        PossibleHandTotals_Rank[cnt]['2'] > 0 and \
        PossibleHandTotals_Rank[cnt]['3'] > 0 and \
        PossibleHandTotals_Rank[cnt]['4'] > 0 and \
        PossibleHandTotals_Rank[cnt]['5'] > 0:
        StraightInfo, StraightInfos = addStraightInfo(cnt, playerHand, \
            highCard, highCardRank, StraightInfo, StraightInfos)
                                        
    if PossibleHandTotals_Rank[cnt]['2'] > 0 and \
        PossibleHandTotals_Rank[cnt]['3'] > 0 and \
        PossibleHandTotals_Rank[cnt]['4'] > 0 and \
        PossibleHandTotals_Rank[cnt]['5'] > 0 and \
        PossibleHandTotals_Rank[cnt]['6'] > 0:
        StraightInfo, StraightInfos = addStraightInfo(cnt, playerHand, \
            highCard, highCardRank, StraightInfo, StraightInfos)
                                                               
    if PossibleHandTotals_Rank[cnt]['3'] > 0 and \
        PossibleHandTotals_Rank[cnt]['4'] > 0 and \
        PossibleHandTotals_Rank[cnt]['5'] > 0 and \
        PossibleHandTotals_Rank[cnt]['6'] > 0 and \
        PossibleHandTotals_Rank[cnt]['7'] > 0:
        StraightInfo, StraightInfos = addStraightInfo(cnt, playerHand, \
            highCard, highCardRank, StraightInfo, StraightInfos)
                                                                  
    if PossibleHandTotals_Rank[cnt]['4'] > 0 and \
        PossibleHandTotals_Rank[cnt]['5'] > 0 and \
        PossibleHandTotals_Rank[cnt]['6'] > 0 and \
        PossibleHandTotals_Rank[cnt]['7'] > 0 and \
        PossibleHandTotals_Rank[cnt]['8'] > 0:
        StraightInfo, StraightInfos = addStraightInfo(cnt, playerHand, \
            highCard, highCardRank, StraightInfo, StraightInfos)
                                                                                   
    if PossibleHandTotals_Rank[cnt]['5'] > 0 and \
        PossibleHandTotals_Rank[cnt]['6'] > 0 and \
        PossibleHandTotals_Rank[cnt]['7'] > 0 and \
        PossibleHandTotals_Rank[cnt]['8'] > 0 and \
        PossibleHandTotals_Rank[cnt]['9'] > 0:
        StraightInfo, StraightInfos = addStraightInfo(cnt, playerHand, \
            highCard, highCardRank, StraightInfo, StraightInfos)
                                                                                         
    if PossibleHandTotals_Rank[cnt]['6'] > 0 and \
        PossibleHandTotals_Rank[cnt]['7'] > 0 and \
        PossibleHandTotals_Rank[cnt]['8'] > 0 and \
        PossibleHandTotals_Rank[cnt]['9'] > 0 and \
        PossibleHandTotals_Rank[cnt]['T'] > 0:
        StraightInfo, StraightInfos = addStraightInfo(cnt, playerHand, \
            highCard, highCardRank, StraightInfo, StraightInfos)
                                                                        
    if PossibleHandTotals_Rank[cnt]['7'] > 0 and \
        PossibleHandTotals_Rank[cnt]['8'] > 0 and \
        PossibleHandTotals_Rank[cnt]['9'] > 0 and \
        PossibleHandTotals_Rank[cnt]['T'] > 0 and \
        PossibleHandTotals_Rank[cnt]['J'] > 0:
        StraightInfo, StraightInfos = addStraightInfo(cnt, playerHand, \
            highCard, highCardRank, StraightInfo, StraightInfos)
                                                                       
    if PossibleHandTotals_Rank[cnt]['8'] > 0 and \
        PossibleHandTotals_Rank[cnt]['9'] > 0 and \
        PossibleHandTotals_Rank[cnt]['T'] > 0 and \
        PossibleHandTotals_Rank[cnt]['J'] > 0 and \
        PossibleHandTotals_Rank[cnt]['Q'] > 0:
        StraightInfo, StraightInfos = addStraightInfo(cnt, playerHand, \
            highCard, highCardRank, StraightInfo, StraightInfos)
                                                                        
    if PossibleHandTotals_Rank[cnt]['9'] > 0 and \
        PossibleHandTotals_Rank[cnt]['T'] > 0 and \
        PossibleHandTotals_Rank[cnt]['J'] > 0 and \
        PossibleHandTotals_Rank[cnt]['Q'] > 0 and \
        PossibleHandTotals_Rank[cnt]['K'] > 0:
            StraightInfo, StraightInfos = addStraightInfo(cnt, playerHand, \
                highCard, highCardRank, StraightInfo, StraightInfos)
                                                                       
    if PossibleHandTotals_Rank[cnt]['T'] > 0 and \
        PossibleHandTotals_Rank[cnt]['J'] > 0 and \
        PossibleHandTotals_Rank[cnt]['Q'] > 0 and \
        PossibleHandTotals_Rank[cnt]['K'] > 0 and \
        PossibleHandTotals_Rank[cnt]['A'] > 0:
            StraightInfo, StraightInfos = addStraightInfo(cnt, playerHand, \
                highCard, highCardRank, StraightInfo, StraightInfos)
                                    
    if len(StraightInfos) == 0:
        StraightInfos.append(StraightInfo)
    
    return StraightInfo, StraightInfos
    
def getFlushes(cnt, playerHand, highCard, highCardRank, FlushInfo, \
    FlushInfos, PossibleHandTotals_Suit):
    if PossibleHandTotals_Suit[cnt][highCard[1]] == 5:
        FlushInfo, FlushInfos = addFlushInfo (cnt, playerHand, \
        highCard, highCardRank, FlushInfo, FlushInfos)
                
    if len(FlushInfos) == 0:
          FlushInfos.append(FlushInfo)
    
    return FlushInfo, FlushInfos    
    
def getStraightFlushes(StraightInfo, FlushInfo, cnt, playerHand, \
    StraightFlushInfo, StraightFlushInfos):
    if StraightInfo['IsPresent'] == 'true' and \
        FlushInfo['IsPresent'] == 'true':
        StraightFlushInfo, StraightFlushInfos = \
            addStraightFlushInfo(StraightInfo, FlushInfo,cnt, \
            playerHand, StraightFlushInfo, StraightFlushInfos)
    if len(StraightFlushInfos) == 0:
        StraightFlushInfos.append(StraightFlushInfo)
    
    
    return StraightFlushInfo, StraightFlushInfos    
    
def getBestStraight(StraightInfo, StraightInfos, highCardRank):
    
    if len(StraightInfos) == 1: 
        for info in StraightInfos:
            if info['IsPresent'] == 'true':
                StraightInfo = info
    elif len(StraightInfos) > 1:
        highCardRank = 0
        for info in StraightInfos:
            if info['IsPresent'] == 'true':
                if info['HighCardRank'] > highCardRank:
                    highCardRank = info['HighCardRank']
                    StraightInfo = info    
    return StraightInfo
    
def getBestFlush(FlushInfo, FlushInfos, highCardRank):
    if len(FlushInfos) == 1:
        for info in FlushInfos:
            if info['IsPresent'] == 'true':
                FlushInfo = info
                break
    elif len(FlushInfos) > 1:
        highCardRank = 0
        for info in FlushInfos:
            if info['IsPresent'] == 'true':
                if info['HighCardRank'] > highCardRank:
                    highCardRank = info['HighCardRank']
                    FlushInfo = info
    
    return FlushInfo
    
def getBestStraightFlush(StraightFlushInfo, StraightFlushInfos, highCardRank):
    
    if len(StraightFlushInfos) == 1:  
        for info in StraightFlushInfos:
            if info['IsPresent'] == 'true':
                StraightFlushInfo = info
                break
    elif len(StraightFlushInfos) > 1:
        highCardRank = 0
        for info in StraightFlushInfos:
            if info['IsPresent'] == 'true':
                if info['HighCardRank'] > highCardRank:
                    highCardRank = info['HighCardRank']
                    StraightFlushInfo = info
    
    return StraightFlushInfo
    
###############################################################################
################ Function Required to determine Straight and flushes in hand ##
###############################################################################
    
def DetermineStraightFlush(player, PlayerHands,PossibleHandTotals_Rank, \
    PossibleHandTotals_Suit, CardRankNumbers):
            
    StraightInfos = []
    FlushInfos = []
    StraightFlushInfos = []

    for cnt, playerHand in enumerate(PlayerHands):
        highCard = ''
        highCardRank = 0
        for card in playerHand:
            if CardRankNumbers[card[0]] > highCardRank:
                highCardRank = CardRankNumbers[card[0]]
                highCard = card
                
        StraightInfo = {'IsPresent':'false'}
        StraightInfo, StraightInfos = getStraights(cnt, playerHand, highCard,\
            highCardRank, StraightInfo, StraightInfos, PossibleHandTotals_Rank)
                          
        FlushInfo = {'IsPresent':'false'}
        FlushInfo, FlushInfos = getFlushes(cnt, playerHand, highCard, \
            highCardRank, FlushInfo, FlushInfos, PossibleHandTotals_Suit)
               
        StraightFlushInfo = {'IsPresent':'false'}
        StraightFlushInfo, StraightFlushInfos = getStraightFlushes(\
            StraightInfo, FlushInfo,cnt, playerHand, StraightFlushInfo, \
            StraightFlushInfos)        
        
    StraightInfo = getBestStraight(StraightInfo, StraightInfos, highCardRank)
    FlushInfo = getBestFlush(FlushInfo, FlushInfos, highCardRank)      
    StraightFlushInfo = getBestStraightFlush(StraightFlushInfo, \
        StraightFlushInfos, highCardRank)
                   
    return StraightFlushInfo, StraightInfo, FlushInfo
    
###############################################################################
############   Functions required to determine player's best hand  ############    
###############################################################################

    
def getBestHand(StraightFlushInfo, StraightInfo, FlushInfo, FourOfAKindInfo,\
    FullHouseInfo,ThreeOfAKindInfo,TwoPairsInfo,OnePairInfo,HighCardInfo):
        
    if StraightFlushInfo['IsPresent'] == 'true':
        BestHand = [StraightFlushInfo]
    elif FourOfAKindInfo['IsPresent'] == 'true':
        BestHand = [FourOfAKindInfo]
    elif FullHouseInfo['IsPresent'] == 'true':
        BestHand = [FullHouseInfo]
    elif FlushInfo['IsPresent'] == 'true':
        BestHand = [FlushInfo]
    elif StraightInfo['IsPresent'] == 'true':
        BestHand = [StraightInfo]
    elif ThreeOfAKindInfo['IsPresent'] == 'true':
        BestHand = [ThreeOfAKindInfo]
    elif TwoPairsInfo['IsPresent'] == 'true':
        BestHand = [TwoPairsInfo]
    elif OnePairInfo['IsPresent'] == 'true':
        BestHand = [OnePairInfo]
    else:
        BestHand = [HighCardInfo]
    
    return BestHand
    
def DetermineBestHand(player, PlayerHands, PossibleHandTotals_Rank, \
            PossibleHandTotals_Suit, CardRankNumbers, CardRanks):
   
    BestHand = {}
         
    StraightFlushInfo, StraightInfo, FlushInfo = \
        DetermineStraightFlush(player, PlayerHands,PossibleHandTotals_Rank,\
        PossibleHandTotals_Suit, CardRankNumbers)
            
    FourOfAKindInfo,FullHouseInfo,ThreeOfAKindInfo,TwoPairsInfo,OnePairInfo, \
        HighCardInfo = DetermineMatches(player, PlayerHands,\
        PossibleHandTotals_Rank,PossibleHandTotals_Suit, CardRankNumbers,
        CardRanks)
        
    BestHand = getBestHand(StraightFlushInfo, StraightInfo, FlushInfo, \
        FourOfAKindInfo, FullHouseInfo, ThreeOfAKindInfo, TwoPairsInfo, \
        OnePairInfo,HighCardInfo)
                  
    return BestHand
    
def DetermineHandTotals(player, PlayerHands, CardRankNumbers, CardRanks):

    PossibleHandTotals_Rank = []
    PossibleHandTotals_Suit = []
       
    for Hand in PlayerHands:
        
        NumberOfCardsOfRank = {'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,\
            '9':0,'T':0, 'J':0,'Q':0,'K':0,'A':0}
        NumberOfCardsOfSuit = {'H':0,'D':0,'C':0,'S':0 }

        NumberOf2s,NumberOf3s,NumberOf4s,NumberOf5s,NumberOf6s,NumberOf7s,\
            NumberOf8s,NumberOf9s,NumberOfTs,NumberOfJs,NumberOfQs,\
            NumberOfKs,NumberOfAs = 0,0,0,0,0,0,0,0,0,0,0,0,0
    
        NumberOfHs,NumberOfDs,NumberOfCs,NumberOfSs = 0,0,0,0

        for card in Hand:
            if card[0] == '2':
                NumberOf2s +=1
            elif card[0] == '3':
                NumberOf3s +=1
            elif card[0] == '4':
                NumberOf4s +=1
            elif card[0] == '5':
                NumberOf5s +=1
            elif card[0] == '6':
                NumberOf6s +=1
            elif card[0] == '7':
                NumberOf7s +=1
            elif card[0] == '8':
                NumberOf8s +=1
            elif card[0] == '9':
                NumberOf9s +=1
            elif card[0] == 'T':
                NumberOfTs +=1
            elif card[0] == 'J':
                NumberOfJs +=1
            elif card[0] == 'Q':
                NumberOfQs +=1
            elif card[0] == 'K':
                NumberOfKs +=1
            elif card[0] == 'A':
                NumberOfAs +=1
                
            if card[1] == 'H':
                NumberOfHs +=1
            elif card[1] == 'D':
                NumberOfDs +=1
            elif card[1] == 'C':
                NumberOfCs +=1
            elif card[1] == 'S':
                NumberOfSs +=1
                                
        NumberOfCardsOfRank['2'] = NumberOf2s
        NumberOfCardsOfRank['3'] = NumberOf3s
        NumberOfCardsOfRank['4'] = NumberOf4s
        NumberOfCardsOfRank['5'] = NumberOf5s
        NumberOfCardsOfRank['6'] = NumberOf6s
        NumberOfCardsOfRank['7'] = NumberOf7s
        NumberOfCardsOfRank['8'] = NumberOf8s
        NumberOfCardsOfRank['9'] = NumberOf9s
        NumberOfCardsOfRank['T'] = NumberOfTs
        NumberOfCardsOfRank['J'] = NumberOfJs
        NumberOfCardsOfRank['Q'] = NumberOfQs
        NumberOfCardsOfRank['K'] = NumberOfKs
        NumberOfCardsOfRank['A'] = NumberOfAs
        
        NumberOfCardsOfSuit['H'] = NumberOfHs
        NumberOfCardsOfSuit['D'] = NumberOfDs
        NumberOfCardsOfSuit['C'] = NumberOfCs
        NumberOfCardsOfSuit['S'] = NumberOfSs
                
        PossibleHandTotals_Rank.append(NumberOfCardsOfRank)
        PossibleHandTotals_Suit.append(NumberOfCardsOfSuit)
        
    BestHand = DetermineBestHand(player,PlayerHands,PossibleHandTotals_Rank,\
        PossibleHandTotals_Suit, CardRankNumbers, CardRanks)
        
    return BestHand

def DeterminePossibleHands(player,PlayerCards, CardRankNumbers, CardRanks):
    
    PlayerHands = makePlayerHands(PlayerCards)
            
    BestHand = DetermineHandTotals(player,PlayerHands, CardRankNumbers, \
        CardRanks)

    return BestHand 
