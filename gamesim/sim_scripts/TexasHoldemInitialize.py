# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 08:29:48 2015

@author: Larry
"""
import json
import mysql.connector
import TexasHoldemInitialize2 as th_i

def getHoleHands(HoleHandPaired_permutations, Suited_permutations, \
    HoleHandNonPaired_permutations):
    DistinctHoleHands = []
    for permutation in HoleHandPaired_permutations:
        DistinctHoleHands.append(permutation)

    for suitType in Suited_permutations:
        for permutation in HoleHandNonPaired_permutations:
            DistinctHoleHands.append(permutation+suitType)
    
    return DistinctHoleHands

def putInitialData():
    
    initialData['python'] = 'C:\\Python34\\Python'
    initialData['parent_process'] = 'Parent_Texas_Holdem_Play.py'
    initialData['child_process'] = 'Child_Texas_Holdem_Play'

    initialData['players_initial'] = ['player0', 'player1', 'player2', \
        'player3', 'player4', 'player5', 'player6', 'player7']

    initialData['card_suits'] = ['H', 'D', 'C', 'S']
    initialData['card_ranks']= ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 
        'J', 'Q', 'K', 'A']
    initialData['card_rank_numbers'] = {'2':2, '3':3, '4':4, '5':5, '6':6, \
        '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

    initialData['hand_types'] = ['HighCard', 'OnePair', 'TwoPairs', \
        'ThreeOfAKind', 'Straight', 'Flush', 'FullHouse', 'FourOfAKind', \
        'StraightFlush']
        
    initialData['hand_type_ranks'] ={'HighCard':1, 'OnePair':2, 'TwoPairs':3, \
        'ThreeOfAKind':4, 'Straight':5, 'Flush':6, 'FullHouse':7, \
        'FourOfAKind':8, 'StraightFlush':9}
                    
    Suited_permutations = ['S', 'NS']
    HoleHandPaired_permutations = ['22', '33', '44', '55', '66', '77', '88',\
        '99', 'TT', 'JJ', 'QQ', 'KK', 'AA']
    HoleHandNonPaired_permutations = ['23', '24', '25', '26', '27', '28', \
        '29', '2T', '2J', '2Q', '2K', '2A', '34', '35', '36', '37', '38', \
        '39', '3T', '3J', '3Q', '3K', '3A', '45', '46', '47', '48', '49', \
        '4T', '4J', '4Q', '4K', '4A', '56', '57', '58', '59', '5T', '5J', \
        '5Q', '5K', '5A', '67', '68', '69' ,'6T', '6J', '6Q', '6K', '6A', \
        '78', '79', '7T', '7J', '7Q', '7K', '7A', '89', '8T', '8J', '8Q', \
        '8K', '8A', '9T', '9J', '9Q', '9K', '9A', 'TJ', 'TQ', 'TK', 'TA', \
        'JQ', 'JK', 'JA', 'QK', 'QA', 'KA']

    permutations = getHoleHands(HoleHandPaired_permutations, \
        Suited_permutations, HoleHandNonPaired_permutations)

    initialData['permutations']=permutations
    
    return
   
def putInitialCounters():
    
    initialCounters['player_wins_initial'] = {'player0':0, 'player1':0, 'player2':0,\
        'player3':0, 'player4':0, 'player5':0, 'player6':0, 'player7':0, \
        'tied':0}
    initialCounters['player_hands_initial'] = {'player0':0, 'player1':0, 'player2':0,\
        'player3':0, 'player4':0, 'player5':0, 'player6':0, 'player7':0, \
        'tied':0}

    initialCounters['hand_type_wins'] = {'HighCard':0, 'OnePair':0, \
        'TwoPairs':0, 'ThreeOfAKind':0, 'Straight':0, 'Flush':0, \
        'FullHouse':0, 'FourOfAKind':0, 'StraightFlush':0}
    initialCounters['hand_type_hands'] = {'HighCard':0, 'OnePair':0, \
        'TwoPairs':0, 'ThreeOfAKind':0, 'Straight':0, 'Flush':0, \
        'FullHouse':0, 'FourOfAKind':0, 'StraightFlush':0}


    initialCounters['hole_hand_wins'] = {'22':0, '33':0, '44':0, \
        '55':0, '66':0, '77':0, '88':0, '99':0, 'TT':0, 'JJ':0, 'QQ':0, \
        'KK':0, 'AA':0, '23S':0, '24S':0, '25S':0, '26S':0, '27S':0, '28S':0,\
        '29S':0, '2TS':0, '2JS':0, '2QS':0, '2KS':0, '2AS':0, '34S':0, \
        '35S':0, '36S':0, '37S':0, '38S':0, '39S':0, '3TS':0, '3JS':0, \
        '3QS':0, '3KS':0, '3AS':0, '45S':0, '46S':0, '47S':0, '48S':0, \
        '49S':0, '4TS':0, '4JS':0, '4QS':0, '4KS':0, '4AS':0, '56S':0, \
        '57S':0, '58S':0, '59S':0, '5TS':0, '5JS':0, '5QS':0, '5KS':0, \
        '5AS':0, '67S':0, '68S':0, '69S':0, '6TS':0, '6JS':0, '6QS':0, \
        '6KS':0, '6AS':0, '78S':0, '79S':0, '7TS':0, '7JS':0, '7QS':0, \
        '7KS':0, '7AS':0, '89S':0, '8TS':0, '8JS':0, '8QS':0, '8KS':0, \
        '8AS':0, '9TS':0, '9JS':0, '9QS':0, '9KS':0, '9AS':0, 'TJS':0, \
        'TQS':0, 'TKS':0, 'TAS':0, 'JQS':0, 'JKS':0, 'JAS':0, 'QKS':0, \
        'QAS':0, 'KAS':0, '23NS':0, '24NS':0, '25NS':0, '26NS':0, '27NS':0, \
        '28NS':0, '29NS':0, '2TNS':0, '2JNS':0, '2QNS':0, '2KNS':0, '2ANS':0,\
        '34NS':0, '35NS':0, '36NS':0, '37NS':0, '38NS':0, '39NS':0, '3TNS':0,\
        '3JNS':0, '3QNS':0, '3KNS':0, '3ANS':0, '45NS':0, '46NS':0, '47NS':0,\
        '48NS':0, '49NS':0, '4TNS':0, '4JNS':0, '4QNS':0, '4KNS':0, '4ANS':0,\
        '56NS':0, '57NS':0, '58NS':0, '59NS':0, '5TNS':0, '5JNS':0, '5QNS':0,\
        '5KNS':0, '5ANS':0, '67NS':0, '68NS':0, '69NS':0, '6TNS':0, '6JNS':0,\
        '6QNS':0, '6KNS':0, '6ANS':0, '78NS':0, '79NS':0, '7TNS':0, '7JNS':0,\
        '7QNS':0, '7KNS':0, '7ANS':0, '89NS':0, '8TNS':0, '8JNS':0, '8QNS':0,\
        '8KNS':0, '8ANS':0, '9TNS':0, '9JNS':0, '9QNS':0, '9KNS':0, '9ANS':0,\
        'TJNS':0, 'TQNS':0, 'TKNS':0, 'TANS':0, 'JQNS':0, 'JKNS':0, 'JANS':0,\
        'QKNS':0, 'QANS':0, 'KANS':0}

    initialCounters['hole_hand_tied_wins'] = {'22':0, '33':0, '44':0,\
        '55':0, '66':0, '77':0, '88':0, '99':0, 'TT':0, 'JJ':0, 'QQ':0, \
        'KK':0, 'AA':0, '23S':0, '24S':0, '25S':0, '26S':0, '27S':0, '28S':0,\
        '29S':0, '2TS':0, '2JS':0, '2QS':0, '2KS':0, '2AS':0, '34S':0, \
        '35S':0, '36S':0, '37S':0, '38S':0, '39S':0, '3TS':0, '3JS':0, \
        '3QS':0, '3KS':0, '3AS':0, '45S':0, '46S':0, '47S':0, '48S':0, \
        '49S':0, '4TS':0, '4JS':0, '4QS':0, '4KS':0, '4AS':0, '56S':0, \
        '57S':0, '58S':0, '59S':0, '5TS':0, '5JS':0, '5QS':0, '5KS':0, \
        '5AS':0, '67S':0, '68S':0, '69S':0, '6TS':0, '6JS':0, '6QS':0, \
        '6KS':0, '6AS':0, '78S':0, '79S':0, '7TS':0, '7JS':0, '7QS':0, \
        '7KS':0, '7AS':0, '89S':0, '8TS':0, '8JS':0, '8QS':0, '8KS':0, \
        '8AS':0, '9TS':0, '9JS':0, '9QS':0, '9KS':0, '9AS':0, 'TJS':0, \
        'TQS':0, 'TKS':0, 'TAS':0, 'JQS':0, 'JKS':0, 'JAS':0, 'QKS':0, \
        'QAS':0, 'KAS':0, '23NS':0, '24NS':0, '25NS':0, '26NS':0, '27NS':0, \
        '28NS':0, '29NS':0, '2TNS':0, '2JNS':0, '2QNS':0, '2KNS':0, '2ANS':0,\
        '34NS':0, '35NS':0, '36NS':0, '37NS':0, '38NS':0, '39NS':0, '3TNS':0,\
        '3JNS':0, '3QNS':0, '3KNS':0, '3ANS':0, '45NS':0, '46NS':0, '47NS':0,\
        '48NS':0, '49NS':0, '4TNS':0, '4JNS':0, '4QNS':0, '4KNS':0, '4ANS':0,\
        '56NS':0, '57NS':0, '58NS':0, '59NS':0, '5TNS':0, '5JNS':0, '5QNS':0,\
        '5KNS':0, '5ANS':0, '67NS':0, '68NS':0, '69NS':0, '6TNS':0, '6JNS':0,\
        '6QNS':0, '6KNS':0, '6ANS':0, '78NS':0, '79NS':0, '7TNS':0, '7JNS':0,\
        '7QNS':0, '7KNS':0, '7ANS':0, '89NS':0, '8TNS':0, '8JNS':0, '8QNS':0,\
        '8KNS':0, '8ANS':0, '9TNS':0, '9JNS':0, '9QNS':0, '9KNS':0, '9ANS':0,\
        'TJNS':0, 'TQNS':0, 'TKNS':0, 'TANS':0, 'JQNS':0, 'JKNS':0, 'JANS':0,\
        'QKNS':0, 'QANS':0, 'KANS':0}

    initialCounters['hole_hand_hands'] = {'22':0, '33':0, '44':0, \
        '55':0, '66':0, '77':0, '88':0, '99':0, 'TT':0, 'JJ':0, 'QQ':0, \
        'KK':0, 'AA':0, '23S':0, '24S':0, '25S':0, '26S':0, '27S':0, '28S':0,\
        '29S':0, '2TS':0, '2JS':0, '2QS':0, '2KS':0, '2AS':0, '34S':0, \
        '35S':0, '36S':0, '37S':0, '38S':0, '39S':0, '3TS':0, '3JS':0, \
        '3QS':0, '3KS':0, '3AS':0, '45S':0, '46S':0, '47S':0, '48S':0, \
        '49S':0, '4TS':0, '4JS':0, '4QS':0, '4KS':0, '4AS':0, '56S':0, \
        '57S':0, '58S':0, '59S':0, '5TS':0, '5JS':0, '5QS':0, '5KS':0, \
        '5AS':0, '67S':0, '68S':0, '69S':0, '6TS':0, '6JS':0, '6QS':0, \
        '6KS':0, '6AS':0, '78S':0, '79S':0, '7TS':0, '7JS':0, '7QS':0, \
        '7KS':0, '7AS':0, '89S':0, '8TS':0, '8JS':0, '8QS':0, '8KS':0, \
        '8AS':0, '9TS':0, '9JS':0, '9QS':0, '9KS':0, '9AS':0, 'TJS':0, \
        'TQS':0, 'TKS':0, 'TAS':0, 'JQS':0, 'JKS':0, 'JAS':0, 'QKS':0, \
        'QAS':0, 'KAS':0, '23NS':0, '24NS':0, '25NS':0, '26NS':0, '27NS':0, \
        '28NS':0, '29NS':0, '2TNS':0, '2JNS':0, '2QNS':0, '2KNS':0, '2ANS':0,\
        '34NS':0, '35NS':0, '36NS':0, '37NS':0, '38NS':0, '39NS':0, '3TNS':0,\
        '3JNS':0, '3QNS':0, '3KNS':0, '3ANS':0, '45NS':0, '46NS':0, '47NS':0,\
        '48NS':0, '49NS':0, '4TNS':0, '4JNS':0, '4QNS':0, '4KNS':0, '4ANS':0,\
        '56NS':0, '57NS':0, '58NS':0, '59NS':0, '5TNS':0, '5JNS':0, '5QNS':0,\
        '5KNS':0, '5ANS':0, '67NS':0, '68NS':0, '69NS':0, '6TNS':0, '6JNS':0,\
        '6QNS':0, '6KNS':0, '6ANS':0, '78NS':0, '79NS':0, '7TNS':0, '7JNS':0,\
        '7QNS':0, '7KNS':0, '7ANS':0, '89NS':0, '8TNS':0, '8JNS':0, '8QNS':0,\
        '8KNS':0, '8ANS':0, '9TNS':0, '9JNS':0, '9QNS':0, '9KNS':0, '9ANS':0,\
        'TJNS':0, 'TQNS':0, 'TKNS':0, 'TANS':0, 'JQNS':0, 'JKNS':0, 'JANS':0,\
        'QKNS':0, 'QANS':0, 'KANS':0}
    
    return
    
def putInitialCounters2():
    
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])    
        
        cur = cnx.cursor()
    
        insert_python_scripts = ("insert into gamesim_python_scripts "
            "(python, parent_process, child_process) "
            "values "
            "(%(python)s, %(parent_process)s, %(child_process)s);")
                                
        insert_data = {'python': initialData['python'] ,'parent_process': \
            initialData['parent_process'], 'child_process': \
            initialData['child_process']}
    
        cur.execute(insert_python_scripts, insert_data)       
        cnx.commit()
        
        insert_cards = ("insert into gamesim_cards "
                        "(card_suits, card_ranks, card_rank_numbers) "
                        "values "
                        "(%(card_suits)s, %(card_ranks)s, "
                        "%(card_rank_numbers)s);")
        
        card_suits1 = json.dumps(initialData['card_suits'])
        card_ranks1 = json.dumps(initialData['card_ranks'])
        card_rank_numbers1 = json.dumps(initialData['card_rank_numbers'])
        
        insert_data = {'card_suits': card_suits1, 'card_ranks': card_ranks1, \
                        'card_rank_numbers': card_rank_numbers1}        
        cur.execute(insert_cards, insert_data)
        cnx.commit()
        
        insert_player = ("insert into gamesim_players "
                "(players_initial, player_wins_initial, player_hands_initial) " 
                "values (%(players_initial)s, %(player_wins_initial)s, "
                "%(player_hands_initial)s);")

        players1 = json.dumps(initialData['players_initial'])                            
        player_wins1 = json.dumps(initialCounters['player_wins_initial'])
        player_hands1 = json.dumps(initialCounters['player_hands_initial'])
        
        insert_data = {'players_initial': players1, 'player_wins_initial': \
            player_wins1, 'player_hands_initial': player_hands1}
            
        cur.execute(insert_player, insert_data)
        cnx.commit()
        
        insert_hands = ("insert into gamesim_hands "
        "(hand_types, hand_type_ranks, hand_type_wins, hand_type_hands) "
        "values (%(hand_types)s, %(hand_type_ranks)s, %(hand_type_wins)s, "
        "%(hand_type_hands)s);")
                        
        hand_types1 = json.dumps(initialData['hand_types'])
        hand_type_ranks1 = json.dumps(initialData['hand_type_ranks'])
        hand_type_wins1 = json.dumps(initialCounters['hand_type_wins'])
        hand_type_hands1 = json.dumps(initialCounters['hand_type_hands'])
        
        insert_data = {'hand_types': hand_types1, 'hand_type_ranks': \
                        hand_type_ranks1, 'hand_type_wins': hand_type_wins1, \
                        'hand_type_hands': hand_type_hands1}
                        
        cur.execute(insert_hands, insert_data) 
        cnx.commit()
        
        insert_hole_hands = ("insert into gamesim_hole_hands "
        "(permutations, hole_hand_wins, hole_hand_tied_wins, hole_hand_hands) "
        "values (%(permutations)s, %(hole_hand_wins)s, %(hole_hand_hands)s, "
        "%(hole_hand_tied_wins)s);")     
        
        permutations1 = json.dumps(initialData['permutations'])
        hole_hand_wins1 = json.dumps(initialCounters['hole_hand_wins'])
        hole_hand_tied_wins1 = json.dumps(initialCounters['hole_hand_tied_wins'])
        hole_hand_hands1 = json.dumps(initialCounters['hole_hand_hands'])
        
        insert_data = {'permutations': permutations1, 'hole_hand_wins': \
                    hole_hand_wins1, 'hole_hand_hands': hole_hand_hands1, \
                    'hole_hand_tied_wins' :hole_hand_tied_wins1}
        cur.execute(insert_hole_hands, insert_data)        
        
        cnx.commit()                
        cnx.close()

    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close
    return
    
def put_grand_summary_data(num_players):
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])    
        cur = cnx.cursor()
        
        insert_grand_summary = ("insert into gamesim_grand_summary_data "
                    "(num_players, player_wins_total, player_hands_total, " 
                    "hand_type_wins_total, hand_type_hands_total, "
                    "hole_hand_wins_total, hole_hand_hands_total, "
                    "hole_hand_tied_wins_total) values (%(num_players)s, "
                    "%(player_wins_total)s, %(player_hands_total)s, "
                    "%(hand_type_wins_total)s, %(hand_type_hands_total)s, "
                    "%(hole_hand_wins_total)s, %(hole_hand_hands_total)s, "
                    "%(hole_hand_tied_wins_total)s); ")
        
        players, player_wins_total, player_hands_total = th_i.putPlayers( \
            num_players, initialData['players_initial'], \
            initialCounters['player_wins_initial'], \
            initialCounters['player_hands_initial'])
        
        player_wins_total = json.dumps(player_wins_total)
        player_hands_total = json.dumps(player_hands_total)
        hand_type_wins_total = json.dumps(initialCounters['hand_type_wins'])
        hand_type_hands_total = json.dumps(initialCounters['hand_type_hands'])
        hole_hand_wins_total = json.dumps(initialCounters['hole_hand_wins'])
        hole_hand_hands_total = json.dumps(initialCounters['hole_hand_hands'])
        hole_hand_tied_wins_total = \
            json.dumps(initialCounters['hole_hand_tied_wins'])
        
        insert_data = {'num_players': str(num_players), 'player_wins_total': \
            player_wins_total, 'player_hands_total': player_hands_total, \
            'hand_type_wins_total':hand_type_wins_total, \
            'hand_type_hands_total': hand_type_hands_total, \
            'hole_hand_wins_total': hole_hand_wins_total, \
            'hole_hand_hands_total': hole_hand_hands_total, \
            'hole_hand_tied_wins_total': hole_hand_tied_wins_total}
        
        cur.execute(insert_grand_summary, insert_data)
        cnx.commit()
        cnx.close
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close        
    return

    


###############################################################################
################# Get Initial Data for Parent Process ############################################
###############################################################################

db_params = {'username':'texasholdem', 'password':'Texasholdem123', \
    'database':'texasholdem_db'}

initialData = {}
initialCounters = {}

putInitialData()
putInitialCounters()


putInitialCounters2()


for num_players in range(2,9):
    put_grand_summary_data(num_players)
    



"""
with open('initialData.txt','w') as d:
    json.dump(initialData,d)
    
with open('initialCounters.txt','w') as d:
    json.dump(initialCounters,d)
"""    

    
    