# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 08:29:48 2015

@author: Larry
"""
import json
import mysql.connector
from random import shuffle


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


def getSimulationParameters(sim_id):
    
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])    
        
        cur = cnx.cursor()
    
        select_sim_parameters = ("select num_players, num_cpus, num_loops, "
                            "num_games, sim_dir from gamesim_simulation_job "
                            "where id = %(sim_id)s;")
        insert_data = {'sim_id': sim_id}
    
        cur.execute(select_sim_parameters, insert_data)
        sim_job1 = cur.fetchone()
        num_Players = int(sim_job1[0])
        num_CPUs = int(sim_job1[1])
        num_Loops = int(sim_job1[2])
        num_Games = int(sim_job1[3])
        sim_dir = sim_job1[4]
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
        
    return num_Players, num_CPUs, num_Loops, num_Games, sim_dir
    
def getSimulationParametersChild(sim_id):
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])    
        
        cur = cnx.cursor()
        select_num_games = ("select num_games, save_game_data from gamesim_simulation_job "
                            "where id = %(sim_id)s;")
        insert_data = {'sim_id': sim_id}
        
        cur.execute(select_num_games, insert_data)
        
        num_games1 = cur.fetchone()
        num_games = int(num_games1[0])
        save_game_data = bool(num_games1[1])
        
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
    
    return num_games, save_game_data
    
def get_python_scripts():
    
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])            
        cur = cnx.cursor()

        select_python_scripts = ("select python, child_process "
                            "from gamesim_python_scripts;")
        cur.execute(select_python_scripts)
        py_scripts = cur.fetchone()
        python = py_scripts[0]
        child_process = py_scripts[1]
    
        cnx.close()
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
    return python, child_process
    
def get_cards():
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])           
        cur = cnx.cursor()
    
        select_cards = ("select card_suits, card_ranks, card_rank_numbers "
                    "from gamesim_cards;")
                    
        cur.execute(select_cards)
        cards1 = cur.fetchone()
        card_suits = json.loads(cards1[0])
        card_ranks = json.loads(cards1[1])
        card_rank_numbers = json.loads(cards1[2])
    
        cnx.close()
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
    return card_suits, card_ranks, card_rank_numbers
    
def get_initial_players():
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])            
        cur = cnx.cursor()

        select_players = ("select players_initial, player_wins_initial, "
                        "player_hands_initial from gamesim_players;")
                    
        cur.execute(select_players)
        players1 = cur.fetchone()
        players = json.loads(players1[0])
        player_wins = json.loads(players1[1])
        player_hands = json.loads(players1[2])
    
        cnx.close()
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
    return players, player_wins, player_hands
    
def get_players():
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])            
        cur = cnx.cursor()

        select_players = ("select players_initial, player_wins, "
                        "player_hands from gamesim_players;")
                    
        cur.execute(select_players)
        players1 = cur.fetchone()
        players = json.loads(players1[0])
        player_wins = json.loads(players1[1])
        player_hands = json.loads(players1[2])
    
        cnx.close()
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
    return players, player_wins, player_hands
    

def get_player_counters():
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])           
        cur = cnx.cursor()

        select_players = ("select player_wins_initial, player_hands_initial "
                    "from gamesim_players;")
                    
        cur.execute(select_players)
        players1 = cur.fetchone()
        player_wins = json.loads(players1[0])
        player_hands = json.loads(players1[1])       
        cnx.close()
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()

    return player_wins, player_hands
    
def get_players_grand_total(num_players):
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])           
        cur = cnx.cursor()

        select_players = ("select player_wins_total, player_hands_total "
                    "from gamesim_grand_summary_data where "
                    "num_players = %(num_players)s;")
                    
        insert_data = {'num_players':num_players}
                    
        cur.execute(select_players, insert_data)
        players1 = cur.fetchone()
        player_wins_grand_total = json.loads(players1[0])
        player_hands_grand_total = json.loads(players1[1])       
        cnx.close()
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()

    return player_wins_grand_total, player_hands_grand_total
    
    
def get_hands():
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])           
        cur = cnx.cursor()
    
        select_hands = ("select hand_types, hand_type_ranks "
                    "from gamesim_hands;")
                
        cur.execute(select_hands)
        hands1 = cur.fetchone()
        hand_types = json.loads(hands1[0])
        hand_type_ranks = json.loads(hands1[1])
    
        cnx.close()
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
    return hand_types, hand_type_ranks
        
def get_hand_counters():
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])           
        cur = cnx.cursor()

        select_hands = ("select hand_type_wins, hand_type_hands "
                    "from gamesim_hands;")
                
        cur.execute(select_hands)
        hands1 = cur.fetchone()
        hand_type_wins = json.loads(hands1[0])
        hand_type_hands = json.loads(hands1[1])
        cnx.close()
        
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
        
    return hand_type_wins, hand_type_hands
    
def get_hand_type_grand_total(num_players):
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])           
        cur = cnx.cursor()

        select_hands = ("select hand_type_wins_total, hand_type_hands_total "
                    "from gamesim_grand_summary_data where "
                    "num_players = %(num_players)s ;")
                    
        insert_data = {'num_players':num_players}
                
        cur.execute(select_hands, insert_data)
        hands1 = cur.fetchone()
        hand_type_wins_grand_total = json.loads(hands1[0])
        hand_type_hands_grand_total = json.loads(hands1[1])
        cnx.close()
        
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
        
    return hand_type_wins_grand_total, hand_type_hands_grand_total
    
    
def get_hole_hands():
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])            
        cur = cnx.cursor()
        select_hole_hands = ("select permutations from gamesim_hole_hands;")        
        cur.execute(select_hole_hands)    
        hole_hands1 = cur.fetchone()
        permutations = json.loads(hole_hands1[0])   
        cnx.close()
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
    return permutations

def get_hole_hand_counters():
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])           
        cur = cnx.cursor()
        
        select_hole_hands = ("select hole_hand_wins, hole_hand_hands, "
            "hole_hand_tied_wins from gamesim_hole_hands;")
        
        cur.execute(select_hole_hands)
        hole_hands1 = cur.fetchone()
        hole_hand_wins = json.loads(hole_hands1[0])
        hole_hand_hands = json.loads(hole_hands1[1])
        hole_hand_tied_wins = json.loads(hole_hands1[2])
        cnx.close()
        
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
        
    return hole_hand_wins, hole_hand_hands, hole_hand_tied_wins
    
def get_hole_hand_grand_total(num_players):
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])           
        cur = cnx.cursor()
        
        select_hole_hands = ("select hole_hand_wins_total, "
            "hole_hand_hands_total, hole_hand_tied_wins_total from "
            "gamesim_grand_summary_data where "
            "num_players = %(num_players)s;")
        
        insert_data = {'num_players':num_players}        
        
        cur.execute(select_hole_hands, insert_data)
        hole_hands1 = cur.fetchone()
        hole_hand_wins_grand_total = json.loads(hole_hands1[0])
        hole_hand_hands_grand_total = json.loads(hole_hands1[1])
        hole_hand_tied_wins_grand_total = json.loads(hole_hands1[2])
        cnx.close()
        
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
        
    return hole_hand_wins_grand_total, hole_hand_hands_grand_total, \
        hole_hand_tied_wins_grand_total

def getInitialCounters():
    
    player_wins_total, player_hands_total = get_player_counters()
    hand_type_wins_total, hand_type_hands_total = get_hand_counters()            
    hole_hand_wins_total, hole_hand_hands_total, \
            hole_hand_tied_wins_total = get_hole_hand_counters()
 
    return player_wins_total, player_hands_total, hand_type_wins_total, \
        hand_type_hands_total, hole_hand_wins_total, \
        hole_hand_hands_total, hole_hand_tied_wins_total
        
def getInitialProbLists():
    player_probs = {}

    hand_type_probs = {}
    hand_type_probs2 = {}

    hole_hand_probs = {}
    hole_hand_probs2 = {}
    hole_hand_norm_probs = {}
    hole_hand_rel_probs = {}
    hole_hand_rel_probs2 = {}    
    return player_probs, hand_type_probs, hand_type_probs2, \
        hole_hand_probs, hole_hand_probs2, \
        hole_hand_norm_probs, hole_hand_rel_probs, \
        hole_hand_rel_probs2
        
def get_game_players():
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])         
        cur = cnx.cursor()
    
        select_players = ("select players_sim, player_wins, player_hands "
                        " from gamesim_players;")
        cur.execute(select_players)
        
        players1 = cur.fetchone()
        players = json.loads(players1[0])
        player_wins = json.loads(players1[1])
        player_hands = json.loads(players1[2])
        cnx.commit()
        cnx.close()

    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
    
    return players, player_wins, player_hands
    
def put_game_players(players_sim):
    
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])         
        cur = cnx.cursor()
    
        select_players = ("select * from gamesim_players;")
        cur.execute(select_players)
        id1 = cur.fetchone()
        id1 = id1[0]
    
        update_game_players = ("update gamesim_players set players_sim = "
                        "%(players_sim)s where id = %(id1)s;")
        insert_data = {'players_sim': json.dumps(players_sim), 'id1':id1}
    
        cur.execute(update_game_players, insert_data)
        cnx.commit()
        cnx.close()
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()

    return
    
def put_player_totals(player_wins, player_hands):
    
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])         
        cur = cnx.cursor()
    
        select_players = ("select id from gamesim_players;")
        cur.execute(select_players)
        id1 = cur.fetchone()
        id1 = id1[0]
    
        update_game_players = ("update gamesim_players set player_wins = "
                        "%(player_wins)s, player_hands = "
                        "%(player_hands)s where id = %(id1)s;")
                        
        insert_data = {'player_wins': json.dumps(player_wins), 'id1':id1, \
                   'player_hands': json.dumps(player_hands)}
                   
        cur.execute(update_game_players, insert_data)
        cnx.commit()
    
        update_game_players = ("update gamesim_players set player_wins_total = "
                        "%(player_wins_total)s, player_hands_total = "
                        "%(player_hands_total)s where id = %(id1)s;")
                        
        insert_data = {'player_wins_total': json.dumps(player_wins), 'id1':id1, \
                   'player_hands_total': json.dumps(player_hands)}
    
        cur.execute(update_game_players, insert_data)
        cnx.commit()
        cnx.close()
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()

    
    return
                
def putPlayers(num_players, players, player_wins_total, player_hands_total):
    players1, player_wins_total1, player_hands_total1 = [],{},{}
    for i, name in enumerate(players):
        if i < num_players:
            players1.append(name)
    for i, key in enumerate(player_wins_total.keys()):
        if i < num_players:
            player_wins_total1['player' + str(i)] = \
                player_wins_total['player' + str(i)] 
            player_hands_total1['player' + str(i)] = \
                player_hands_total['player' + str(i)]
    player_wins_total1['tied'] = player_wins_total['tied']
    player_hands_total1['tied'] = player_hands_total['tied']
    
    put_game_players(players1)
    print(player_wins_total1)
    print(player_hands_total1)
    
    put_player_totals(player_wins_total1, player_hands_total1)
    
    print(player_wins_total1)
    print(player_hands_total1)

                
    return players1, player_wins_total1,player_hands_total1

def getPlayerCounters():
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])            
        cur = cnx.cursor()
    
        select_player_counters = ("select player_wins, player_hands "
                            "from gamesim_players;")
                            
        cur.execute(select_player_counters)
        counter1 = cur.fetchone()
        player_wins =json.loads(counter1[0])
        player_hands = json.loads(counter1[1])

        cnx.close()    
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()

    return player_wins, player_hands
    
###############################################################################
##############  Initialization Functions for Game #############################
###############################################################################
def get_running_job():
    
    try:
        cnx = mysql.connector.connect(user=db_params['username'], password = \
            db_params['password'], database= db_params['database'])    
        cur = cnx.cursor()
    
        select_running_job = ("select * from gamesim_simulation_job "
                        "where status = 'running'; ")
    
        cur.execute(select_running_job)
        
        running_job = cur.fetchone()
        
        if running_job is None:
            running_job = []
            print('Turn on your dispatcher, dummy!')
            
        cnx.close()
        
    except mysql.connector.Error as e:
        print(e.args[0])
        print(e.args[1])
        cnx.close()
    return running_job[3]
    
def getGameParameters():
    
    numberOfTieGames = 0
    numberOfNonTieGames = 0
    totalNumberOfGames = 0

    NonTiedGames = []
    TiedGames = [] 
    
    return numberOfTieGames, numberOfNonTieGames, totalNumberOfGames, \
        NonTiedGames, TiedGames
        
def getInitialCardLists(Players):
    PlayerCards = {}
    CardsNotAvailableToEachPlayer = {}

    HoleCards = {}
    FlopCards = []
    RiverCard = []
    TurnCard = []
    
    for player in Players:
        HoleCards[player] = []
        CardsNotAvailableToEachPlayer[player]=[]
        PlayerCards[player] = []    

    return PlayerCards, CardsNotAvailableToEachPlayer, HoleCards, FlopCards,\
        RiverCard, TurnCard
        
###############################################################################
################ Function to Generate Shuffled Deck ###########################
###############################################################################

def getShuffledDeck(CardSuits, CardRanks):
    shuffle(CardSuits)
    shuffle(CardRanks)
    
    PlayingCards3 = []
    for cardSuit in CardSuits:
        for cardRank in CardRanks:
            PlayingCards3.append((cardRank,cardSuit))

    Deck = PlayingCards3
    shuffle(Deck)
    shuffle(Deck)
    
    return Deck
    
###############################################################################
######## Function to Deal Hole Cards ##########################################
###############################################################################

def getHoleCards(cnt, Players, HoleCards, PlayerCards, Deck):

    for i in range(2):   
        for player in Players:
            HoleCards[player].append(Deck[cnt])
            PlayerCards[player].append(Deck[cnt])
            Deck.__delitem__(cnt)
            cnt +=1
    
    for player in Players:
        HoleCards[player] = tuple(HoleCards[player])
            
    return cnt

###############################################################################
##########  Function to Deal Flop Cards  ######################################
###############################################################################
def getFlopCards(cnt, FlopCards, Players, PlayerCards, Deck):
    for i in range(3):
        FlopCards.append(Deck[cnt])
        for player in Players:
            PlayerCards[player].append(Deck[cnt])        
        Deck.__delitem__(cnt)
        cnt +=1
    FlopCards = tuple(FlopCards)
    
    return cnt
    
###############################################################################
##########  Function to Deal Turn Card  ######################################
###############################################################################
    
def getTurnCard(cnt, TurnCard, Players, PlayerCards, Deck):

    TurnCard.append(Deck[cnt])
    for player in Players:
        PlayerCards[player].append(Deck[cnt])        
    Deck.__delitem__(cnt)
    cnt +=1
    TurnCard = tuple(TurnCard)
    
    return cnt
    
###############################################################################
##########  Function to Deal River Card  ######################################
###############################################################################
def getRiverCard(cnt, RiverCard, Players, PlayerCards, Deck):

    RiverCard.append(Deck[cnt])
    for player in Players:
        PlayerCards[player].append(Deck[cnt])        
    Deck.__delitem__(cnt)
    cnt +=1
    RiverCard = tuple(RiverCard)
    
    return cnt

    
###############################################################################
################# Get Initial Data for Parent Process ############################################
###############################################################################

db_params = {'username':'texasholdem', 'password':'Texasholdem123', \
    'database':'texasholdem_db'}

###############################################################################
############### Calulate and Put Grand Total Aggreates ########################
###############################################################################



def combinePlayerTotals(num_players, player_wins_total, \
    player_hands_total, player_wins_grand_total, player_hands_grand_total):
    
    for player in player_wins_total.keys():
        player_wins_grand_total[player] = player_wins_grand_total[player] + \
            player_wins_total[player]
        player_hands_grand_total[player] = player_hands_grand_total[player] + \
            player_hands_total[player]
            
    return player_wins_grand_total, player_hands_grand_total
    
def combineHandTypeTotals(num_players, hand_types, hand_type_wins_total, \
    hand_type_hands_total, hand_type_wins_grand_total, \
    hand_type_hands_grand_total):
    
    for i, hand_type in enumerate(hand_types):
        hand_type_wins_grand_total[hand_type] = hand_type_wins_grand_total[hand_type] +\
            hand_type_wins_total[hand_type]
        hand_type_hands_grand_total[hand_type] = hand_type_hands_grand_total[hand_type] +\
            hand_type_hands_total[hand_type]
            
    return hand_type_wins_grand_total, hand_type_hands_grand_total
    
def combineHoleHandTotals(num_players, permutations, hole_hands_wins_total, \
    hole_hands_hands_total, hole_hands_tied_wins_total, \
    hole_hands_wins_grand_total, hole_hands_hands_grand_total, \
    hole_hands_tied_wins_grand_total):
    
    for i, permutation in enumerate(permutations):
        
            hole_hands_wins_grand_total[permutation] = \
                hole_hands_wins_total[permutation] + \
                + hole_hands_wins_total[permutation]
            hole_hands_hands_grand_total[permutation] = \
                hole_hands_hands_grand_total[permutation] + \
                hole_hands_hands_total[permutation]
            hole_hands_tied_wins_grand_total[permutation] = \
                hole_hands_tied_wins_grand_total[permutation] + \
                hole_hands_tied_wins_grand_total[permutation]
            
    return hole_hands_wins_grand_total, hole_hands_hands_grand_total, \
        hole_hands_tied_wins_grand_total

def putGrandTotals(num_players, player_wins_grand_total, \
    player_hands_grand_total, hand_type_wins_grand_total, \
    hand_type_hands_grand_total, hole_hands_wins_grand_total, \
    hole_hands_hands_grand_total, hole_hands_tied_wins_grand_total):
         
        try:
            cnx = mysql.connector.connect(user=db_params['username'], password = \
                db_params['password'], database= db_params['database'])    
            cur = cnx.cursor()
            
            """
            select_players = ("select num_players from gamesim_grand_summary_data;")
            cur.execute(select_players)
            id1 = cur.fetchone()
            id1 = id1[0]
            """
            update_grand_summary = ("update gamesim_grand_summary_data "
              "set player_wins_total = %(player_wins_total)s, "
              "player_hands_total = %(player_hands_total)s, "
              "hand_type_wins_total = %(hand_type_wins_total)s, "
              "hand_type_hands_total = %(hand_type_hands_total)s, "
              "hole_hand_wins_total = %(hole_hand_wins_total)s, "
              "hole_hand_hands_total = %(hole_hand_hands_total)s, "
              "hole_hand_tied_wins_total = %(hole_hand_tied_wins_total)s "
              "where num_players = %(num_players)s;")
                        
            insert_data = {'num_players':num_players,\
              'player_wins_total': \
                  json.dumps(player_wins_grand_total),\
              'player_hands_total': \
                  json.dumps(player_hands_grand_total), \
              'hand_type_wins_total': \
                  json.dumps(hand_type_wins_grand_total), \
              'hand_type_hands_total': \
                  json.dumps(hand_type_hands_grand_total), \
              'hole_hand_wins_total': \
                  json.dumps(hole_hands_wins_grand_total), \
              'hole_hand_hands_total': \
                  json.dumps(hole_hands_hands_grand_total), \
              'hole_hand_tied_wins_total': \
                  json.dumps(hole_hands_tied_wins_grand_total)}
                   
            cur.execute(update_grand_summary, insert_data)
            cnx.commit()
            
        except mysql.connector.Error as e:
            print(e.args[0])
            print(e.args[1])
            cnx.close()
        
def getGrandTotalGames(total_number_of_games2, player_wins_grand_total):
    grand_total_number_of_games = 0
    for wins in player_wins_grand_total.values():
        grand_total_number_of_games = grand_total_number_of_games + wins
    return grand_total_number_of_games