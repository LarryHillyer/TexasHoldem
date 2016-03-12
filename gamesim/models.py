from django.db import models
import jsonfield
import datetime as dt
from django.utils import timezone

root_dir = 'C:\\Users\\Larry\\SkyDrive\\Python\\Django\\TexasHoldem\\'
app_dir = 'gamesim\\'
sim_script_dir = 'sim_scripts\\'

CPU_CHOICES = (('1', '1'), ('2','2'), ('3','3'))
PLAYER_CHOICES = (('2','2 Players'), ('3','3 Players'), ('4','4 Players'), \
    ('5','5 Players'), ('6','6 Players'), ('7','7 Players'), ('8','8 Players'))
STATUS_CHOICES = (('Stopped','Stopped'), ('Idle','Idle'), \
    ('Running', 'Running'), ('Finished','Finished') )


class Simulation_Job(models.Model):

    job_name = models.CharField(max_length = 30, null = True, unique = True)
    status = models.CharField(max_length = 10, default = 'pending')
    run_time = models.DateTimeField(null = True)
    finish_time = models.DateTimeField(null = True)
    
    num_players = models.CharField(max_length = 2, choices = PLAYER_CHOICES, \
        default = '2')
    num_cpus = models.CharField(max_length = 3, choices = CPU_CHOICES, \
        default = '3')
    num_loops = models.CharField(max_length = 5, default = '10')
    num_games = models.CharField(max_length = 12, default = '1000')
    
    sim_dir = models.CharField(max_length = 200 , default = \
        root_dir+app_dir+sim_script_dir)
        
    summary_data = jsonfield.JSONField(null = True)
    save_game_data = models.BooleanField(default = False)
    
    class Meta:
        ordering = ('run_time',)
    
    def __str__(self):
        dt1 =self.run_time
        return dt.datetime.strftime(dt1, '%Y-%m-%d %H:%M:%S')
        
    

class cpu1loopdata(models.Model):
    
    simulation_job = models.ForeignKey(Simulation_Job)
    run_time = models.DateTimeField()
    num_players = models.IntegerField()
    cpu_num = models.CharField(max_length = 3)
    non_tied_hands = jsonfield.JSONField(null=True)
    tied_hands = jsonfield.JSONField(null=True)
    parent_data = jsonfield.JSONField('loop summary data returned to parent')
    
    def __str__(self):
        dt1 =self.run_time
        return dt.datetime.strftime(dt1, '%Y-%m-%d %H:%M:%S')
    
    def was_ran_today(self):
        return self.runtime >= timezone.now() - dt.timedelta(days=1)

    was_ran_today.admin_order_field = 'run_time'
    was_ran_today.boolean = True
    was_ran_today.short_description = 'Ran Today?'

class cpu2loopdata(models.Model):
    
    simulation_job = models.ForeignKey(Simulation_Job)    
    run_time = models.DateTimeField()
    num_players = models.IntegerField()
    cpu_num = models.CharField(max_length = 3)
    non_tied_hands = jsonfield.JSONField(null=True)
    tied_hands = jsonfield.JSONField(null=True)
    parent_data = jsonfield.JSONField('loop summary data returned to parent')
    
    def __str__(self):
        return self.run_time
    
    def was_ran_today(self):
        return self.runtime >= timezone.now() - dt.timedelta(days=1)
        
    was_ran_today.admin_order_field = 'run_time'
    was_ran_today.boolean = True
    was_ran_today.short_description = 'Ran Today?'

class cpu3loopdata(models.Model):
    
    simulation_job = models.ForeignKey(Simulation_Job)    
    run_time = models.DateTimeField()
    num_players = models.IntegerField()
    cpu_num = models.CharField(max_length = 3)
    non_tied_hands = jsonfield.JSONField(null=True)
    tied_hands = jsonfield.JSONField(null=True)
    parent_data = jsonfield.JSONField('loop summary data returned to parent')

    def __str__(self):
        return self.run_time
        
    def was_ran_today(self):
        return self.runtime >= timezone.now() - dt.timedelta(days=1)

    was_ran_today.admin_order_field = 'run_time'
    was_ran_today.boolean = True

class dispatcher_status(models.Model):
      
    status = models.CharField(max_length = 8, choices = STATUS_CHOICES, \
        default = 'Stopped')
    job_name = models.CharField(max_length = 30, null = True)
    
class dispatcher_status2(models.Model):
      
    status = models.CharField(max_length = 8, choices = STATUS_CHOICES, \
        default = 'Stopped')
    job_name = models.CharField(max_length = 30, null = True)

    
class dispatcher_time(models.Model):
    time_delta = models.TimeField(null = True)
    
class dispatcher_time2(models.Model):
    time_delta = models.TimeField(null = True)
    

    
class loop_status(models.Model):
    job_name = models.CharField(max_length = 30, )
    loop_num = models.CharField(max_length = 4, )
    loop_time = models.CharField(max_length = 30, )    
    cpu1_exit_status = models.CharField(max_length = 3, )
    cpu2_exit_status = models.CharField(max_length = 3, )
    cpu3_exit_status = models.CharField(max_length = 3, )
    
    
class python_scripts(models.Model):
    python = models.CharField(max_length = 25, )
    parent_process = models.CharField(max_length = 30, )
    child_process = models.CharField(max_length = 25, )

class players(models.Model):
    players_initial = jsonfield.JSONField() 
    player_wins_initial = jsonfield.JSONField()
    player_hands_initial = jsonfield.JSONField()
    
    players_sim = jsonfield.JSONField(null=True) 
    player_wins = jsonfield.JSONField(null=True)
    player_hands = jsonfield.JSONField(null=True)
    player_wins_total = jsonfield.JSONField(null=True)
    player_hands_total = jsonfield.JSONField(null=True)
    
    def get_players():
        players1 = players.objects.all()[0]
        return players1.players_initial, players1.player_wins_initial, \
            players1.player_hands_initial
            
    def get_game_players(num_players, players1, player_wins_total, \
        player_hands_total):
        players1_1, player_wins_total1, player_hands_total1 = [],{},{}
        for i, name in enumerate(players1):
            if i < num_players:
                players1_1.append(name)  
        for i, key in enumerate(player_wins_total.keys()):
            if i < num_players:
                player_wins_total1['player' + str(i)] = \
                    player_wins_total['player' + str(i)] 
                player_hands_total1['player' + str(i)] = \
                    player_hands_total['player' + str(i)]
        player_wins_total1['tied'] = player_wins_total['tied']
        player_hands_total1['tied'] = player_hands_total['tied']
                    
        return players1_1, player_wins_total1,player_hands_total1
        

class cards(models.Model):
    card_suits = jsonfield.JSONField()
    card_ranks = jsonfield.JSONField()
    card_rank_numbers = jsonfield.JSONField()
    
    def get_cards():
        cards1 = cards.objects.all()[0]
        return cards1.card_suits, cards1.card_ranks, cards1.card_rank_numbers
        
    
class hands(models.Model):
    hand_types = jsonfield.JSONField()
    hand_type_ranks = jsonfield.JSONField()
    hand_type_wins = jsonfield.JSONField(null=True)
    hand_type_hands = jsonfield.JSONField(null=True)
    
    def get_hands():
        hands1 = hands.objects.all()[0]
        return hands1.hand_types, hands1.hand_type_ranks, hands1.hand_type_wins, \
            hands1.hand_type_hands
    
class hole_hands(models.Model):
    permutations= jsonfield.JSONField()
    hole_hand_wins = jsonfield.JSONField(null=True)
    hole_hand_tied_wins = jsonfield.JSONField(null=True)
    hole_hand_hands = jsonfield.JSONField(null=True)
    hole_hand_wins_total = jsonfield.JSONField(null=True)
    
    def get_hole_hands():
        hole_hands1 = hole_hands.objects.all()[0]
        return hole_hands1.permutations, hole_hands1.hole_hand_wins, \
            hole_hands1.hole_hand_tied_wins, hole_hands1.hole_hand_hands
            
class grand_summary_data(models.Model):
    
    num_players = models.CharField(max_length = 2, choices = PLAYER_CHOICES, \
        default = '2')
    
    player_wins_total = jsonfield.JSONField(null=True)
    player_hands_total = jsonfield.JSONField(null=True)
    hand_type_wins_total = jsonfield.JSONField(null=True)
    hand_type_hands_total = jsonfield.JSONField(null=True)
    hole_hand_wins_total = jsonfield.JSONField(null=True)
    hole_hand_tied_wins_total = jsonfield.JSONField(null=True)
    hole_hand_hands_total = jsonfield.JSONField(null=True)
    analyzed_gs_data = jsonfield.JSONField(null=True)
    
    
class finished_jobs(models.Model):

    job_name = models.CharField(max_length = 30, null = True, unique = True)
    status = models.CharField(max_length = 10, default = 'pending')
    run_time = models.DateTimeField(null = True)
    finish_time = models.DateTimeField(null = True)
    
    num_players = models.CharField(max_length = 2, choices = PLAYER_CHOICES, \
        default = '2')
    num_cpus = models.CharField(max_length = 3, choices = CPU_CHOICES, \
        default = '3')
    num_loops = models.CharField(max_length = 5, default = '10')
    num_games = models.CharField(max_length = 12, default = '1000')
    
    sim_dir = models.CharField(max_length = 200 , default = \
        root_dir+app_dir+sim_script_dir)
        
    summary_data = jsonfield.JSONField(null = True)
    save_game_data = models.BooleanField(default = False)
    
    class Meta:
        ordering = ('run_time',)
    
    def __str__(self):
        dt1 =self.run_time
        return dt.datetime.strftime(dt1, '%Y-%m-%d %H:%M:%S')

class analyzed_jobs(models.Model):
    
    job_name = models.CharField(max_length = 30, null = True, unique = True)
    sim_job_names = jsonfield.JSONField(null = True)
    status = models.CharField(max_length = 10, default = 'pending')
    run_time = models.DateTimeField(null = True)
    finish_time = models.DateTimeField(null = True)
    
    num_players = models.CharField(max_length = 2, default = '2')
    
    sim_dir = models.CharField(max_length = 200 , default = \
        root_dir+app_dir+sim_script_dir)
        
    summary_data = jsonfield.JSONField(null = True)
    analyzed_files = jsonfield.JSONField(null = True)
    analyzed_job_data = jsonfield.JSONField(null=True)
    num_games = models.CharField(max_length =20, null = True)
    grand_num_games = models.CharField(max_length = 20, null = True)
    
    
    class Meta:
        ordering = ('run_time',)
    
    def __str__(self):
        dt1 =self.run_time
        return dt.datetime.strftime(dt1, '%Y-%m-%d %H:%M:%S')

class analyze_job_status(models.Model):
    
    job_name = models.CharField(max_length = 30)
    p_pc_status = models.CharField(max_length = 10, default = 'pending')
    ht_bc_status = models.CharField(max_length = 10, default = 'pending')
    ht_pt_status = models.CharField(max_length = 10, default = 'pending')
    rp_t_status = models.CharField(max_length = 10, default = 'pending')    
    sp_status = models.CharField(max_length = 10, default = 'pending')
    ns_np_cp_status = models.CharField(max_length = 10, default = 'pending')
    s_np_cp_status = models.CharField(max_length = 10, default = 'pending')
    p_cp_status = models.CharField(max_length = 10, default = 'pending')    
    rp_bc_status = models.CharField(max_length = 10, default = 'pending')
    rp_sp_status = models.CharField(max_length = 10, default = 'pending')
    pw_p_status = models.CharField(max_length = 10, default = 'pending')
    pw_t_status = models.CharField(max_length = 10, default = 'pending')
   