from django.shortcuts import render
from django.http import HttpResponse, Http404
#from django.core.urlresolvers import reverse
from django.db.models import Q


from gamesim.models import Simulation_Job , python_scripts, cards, hands, \
    hole_hands, players,  dispatcher_time, dispatcher_status, loop_status, \
    dispatcher_time2, dispatcher_status2, finished_jobs, analyzed_jobs, \
    analyze_job_status, grand_summary_data

#from gamesim.forms import dispatcher_status_form
        
from gamesim.serializers import Simulation_Job_Serializer, \
    dispatcher_status_serializer, loop_status_serializer, \
    dispatcher_time_serializer, analyzed_jobs_serializer, \
    finished_jobs_serializer, analyze_job_status_serializer, \
    dispatcher_status2_serializer, dispatcher_time2_serializer, \
    analyzed_jobs2_serializer
    

from rest_framework.decorators import  APIView 
from rest_framework import status
from rest_framework.response import Response

import datetime as dt
import math
import json
import subprocess
import pytz
import numpy as np

root_dir = 'C:\\Users\\Larry\\SkyDrive\\Python\\Django\\TexasHoldem\\'
app_dir = 'gamesim\\'
sim_script_dir = 'sim_scripts\\'

initial_script = 'TexasHoldemInitialize.py'
job_script = 'Job_Dispatcher.py'
job_script2 = 'Job_Dispatcher2.py'

analyze_script = 'Texas_Holdem_AnalyzeStats.py'

sim_dir = root_dir + app_dir + sim_script_dir


try:
    ds1 = dispatcher_status.objects.get(pk=1)
    if ds1.status == 'Reset':
        ds1.status = 'Stopped'
        ds1.job_name = ''
        ds1.save()
        print('save')
except dispatcher_status.DoesNotExist:
    ds1 = dispatcher_status.objects.all().delete()
    ds1 = dispatcher_status(status = 'Stopped')
    dsd = ds1.id
    ds1.id = 1
    ds1.save()
    
class index(APIView):
 
    def get(self, request):
        
        return render(request,'gamesim/index.html') 
                
class get_sim_form_data(APIView):
    
    def get_job_object(self, pk):
        try:
            ds1 = dispatcher_status.objects.get(pk=pk)
            if ds1.status == 'Reset':
                ds1.status = 'Stopped'
                ds1.job_name = ''
                ds1.save()           
            return ds1
        except:
            ds1 = dispatcher_status.objects.all().delete()
            ds1 = dispatcher_status(status = 'Stopped')
            ds1.id = 1
            ds1.save()
            return ds1
            
    def get_loop_status_objects(self):
        try:
            return loop_status.objects.all()
        except:
            raise Http404
    
    def get(self,request):
        
        dispatcher_status1 = self.get_job_object(pk=1)
        if dispatcher_status1.status == 'Finished':
            dispatcher_status1.status = 'Stopped'
            dispatcher_status1.save()
            
        loop_status1 = self.get_loop_status_objects()
        loop_status1.delete()
        
        sim_form_data = {'num_players':'2', 'num_cpus':'3', 'num_loops':'10', \
            'num_games':'1000', 'sim_dir': sim_dir,}
            
        sim_form_data = json.dumps(sim_form_data)
        print(sim_form_data)
        return Response(sim_form_data)
        
class put_sim_form_data(APIView):
    
    def post(self,request):
        print(request.POST)
        sim_form_data = request.POST['sim_form_data']
        sim_form_data = json.loads(sim_form_data)
        print(sim_form_data['num_games'])
        print(sim_form_data['save_game_data'])
        #form = Simulation_Job_Form1(request.POST)
                      
        sim = Simulation_Job( job_name = 'sim', 
            num_players = sim_form_data['num_players'], \
            num_cpus = sim_form_data['num_cpus'], \
            num_loops = sim_form_data['num_loops'], \
            num_games = sim_form_data['num_games'], \
            run_time = dt.datetime.now(pytz.utc), \
            save_game_data = sim_form_data['save_game_data'], \
            sim_dir = sim_form_data['sim_dir'])
    
        sim.save()
        sim.job_name = 'sim' + str(sim.id)
        sim.save()
        return Response()
        
class get_pending_job_list(APIView):
    
    def get_sim_object(self, status):
        try:
            return Simulation_Job.objects.filter(status=status)
        except Simulation_Job.DoesNotExist:
            raise Http404
            
    def get_job_object(self, pk):
        try:
            ds1 = dispatcher_status.objects.get(pk=pk)
            if ds1.status == 'Reset':
                ds1.status = 'Stopped'
                ds1.job_name = ''
                ds1.save()           
            return ds1
        except:
            ds1 = dispatcher_status.objects.all().delete()
            ds1 = dispatcher_status(status = 'Stopped')
            ds1.id = 1
            ds1.save()
            return ds1
            
    def get_loop_status_objects(self):
        try:
            return loop_status.objects.all()
        except:
            raise Http404
                     
    def get(self, request):
        print("get pending jobs")
        pending_job_list = None
        dispatch_status1 = self.get_job_object(pk=1)
        if dispatch_status1.status == 'Stopped':
            pending_job_list = self.get_sim_object(status = 'pending')
        elif dispatch_status1.status == 'Finished':
            dispatch_status1.status = 'Stopped'
            dispatch_status1.save()
            pending_job_list = self.get_sim_object(status = 'pending')            
        
        loop_status1 = self.get_loop_status_objects()
        loop_status1.delete()        
        
        #form = Simulation_Job_Form2()
        #context = {'pending_job_list':pending_job_list, 'form':form}
        print(pending_job_list)
        pending_job_list1 = Simulation_Job_Serializer(pending_job_list, many=True)
        print(pending_job_list1.data)
        return Response(pending_job_list1.data)
        
class get_sim_job(APIView):
    
    def get_sim_object(self, job_name):
        try:
            return Simulation_Job.objects.filter(job_name=job_name)
        except Simulation_Job.DoesNotExist:
            raise Http404
            
    def post(self,request):
        print(request.POST)
        job_name = request.POST['get_sim_job']
        print(job_name)
        requested_job = self.get_sim_object(job_name)
        print(requested_job)
        requested_job = Simulation_Job_Serializer(requested_job[0])
        return Response(requested_job.data)
        
    
        
class delete_sim_job(APIView):
    
    def get_sim_object(self, job_name):
        try:
            return Simulation_Job.objects.filter(job_name=job_name)
        except Simulation_Job.DoesNotExist:
            raise Http404
    
    def post(self, request):
        print(request.POST)
        job_name = request.POST['delete_sim_job']
        print(job_name)
        #job_name = json.loads(job_name)
        deleted_job = self.get_sim_object(job_name)
        deleted_job.delete()
        return Response()
        
class start_dispatcher(APIView):
    
    def get_object(self, pk):
        try:
            return dispatcher_status.objects.get(pk=pk)
        except dispatcher_status.DoesNotExist:
            raise Http404
            
    def get_loop_status_objects(self):
        try:
            return loop_status.objects.all()
        except:
            raise Http404
    
    
    def get_first_job_id(self, status):      
        try:
            jobs = Simulation_Job.objects.filter(status=status)
            min_run_time = jobs[0].run_time
            first_job = jobs[0]
            if jobs.count() > 1:
                for i, job in enumerate(jobs, 1):
                    if job.run_time < min_run_time:
                        min_run_time = job.run_time
                        first_job = job
            return first_job.id
        except:
            raise Http404    
    
    def get(self,request):
        
        loop_status1 = self.get_loop_status_objects()
        loop_status1.delete()
        print("loop status")
        first_job_id = self.get_first_job_id(status='pending')
        args = ['python',  sim_dir + job_script, str(first_job_id)]
        subprocess.Popen(args, stdout = subprocess.PIPE)
        
        dispatcher_status1 =  self.get_object(pk=1)
        print("dispatcher status")
        if dispatcher_status1.status == 'Finished':
            dispatcher_status1.status = 'Stopped'
            dispatcher_status1.save()
        
        dispatcher_status1 = dispatcher_status_serializer(dispatcher_status1)
        return Response(dispatcher_status1.data)
    
class get_dispatcher_status1(APIView):
    
    def get_object(self, pk):
        try:
            return dispatcher_status.objects.get(pk=pk)
        except dispatcher_status.DoesNotExist:
            raise Http404    
    
    def get(self, request):
        dispatcher_status1 =  self.get_object(pk=1)
        print("dispatcher status")
        if dispatcher_status1.status == 'Finished':
            dispatcher_status1.status = 'Stopped'
            dispatcher_status1.save()
        
        dispatcher_status1 = dispatcher_status_serializer(dispatcher_status1)
        return Response(dispatcher_status1.data)

class get_dispatcher_time1(APIView):
    
    def get_object(self, job_name):
        try:
            return Simulation_Job.objects.get(job_name=job_name)
        except dispatcher_status.DoesNotExist:
            raise Http404
      
    def post(self,request):
        print("dispatcher time")
        print(request.POST)
        job_name = request.POST['running_job_name']
        print(job_name)
        #job_name =json.loads(job_name)
        dispatcher_status1 = self.get_object(job_name)
        initial_time = dispatcher_status1.run_time
        current_time = dt.datetime.now(pytz.utc)
        job_time = current_time - initial_time
        hrs = math.floor(job_time.seconds/3600)
        min_secs = job_time.seconds - hrs*3600 
        mins = math.floor(min_secs/60)
        secs = min_secs - mins*60
        time_delta = dt.time(hour=hrs, minute=mins, second=secs)
        dispatcher_time1 = dispatcher_time(time_delta=time_delta)
        serializer = dispatcher_time_serializer(dispatcher_time1)
        return Response(serializer.data)
        
class get_loop_status1(APIView):
    
    def get_object(self):
        try:
            return loop_status.objects.all()
        except loop_status.DoesNotExist:
            raise Http404
          
    def get(self, request):
        loops = self.get_object()
        serializer = loop_status_serializer(loops, many = True)
        return Response(serializer.data)
        
class reset_dispatcher(APIView):
    
    def set_object(self):
        try:
            ds1 = dispatcher_status.objects.get(pk=1)
            if ds1.status != 'Reset':
                ds1.status = 'Reset'
                ds1.save()
        except:
            ds1 = dispatcher_status.objects.all().delete()
            ds1 = dispatcher_status(status = 'Reset')
            ds1.id = 1
            ds1.save()      
        try:
            sj1 = Simulation_Job.objects.get(status='running')
            sj1.status ='aborted'
            sj1.save()
        except:
            pass
        return
   
    def get(self,request):
        
        self.set_object()
        return Response("")

class put_analyze_form_data(APIView):

    def post(self,request):
        
        analyze_form_data = json.loads(request.POST['analyze_form_data'])
        num_players = analyze_form_data['num_players']
        start_date = analyze_form_data['start_date']
        start_date = start_date.split('T')[0]
        start_date = dt.datetime.strptime(start_date,'%Y-%m-%d')
        end_date =analyze_form_data['end_date']
        end_date = end_date.split('T')[0]
        end_date = dt.datetime.strptime(end_date,'%Y-%m-%d')
        start_datetime = dt.datetime(year=start_date.year, month = \
            start_date.month, day = start_date.day, hour = 0, minute = 0, \
            second = 0).replace(tzinfo=pytz.utc)
        end_datetime = dt.datetime(year=end_date.year, month = \
            end_date.month, day = end_date.day, hour = 23, minute = 59, \
            second = 59).replace(tzinfo=pytz.utc)
        finished_job_list = finished_jobs.objects.all().delete()                      
        finished_job_list = Simulation_Job.objects.filter( \
            Q(run_time__gte = start_datetime) & Q(run_time__lte = \
            end_datetime), num_players = num_players, status = 'finished' )
        for job in finished_job_list:
            finished_job = finished_jobs(job_name = job.job_name, \
                status = job.status, run_time = job.run_time, finish_time \
                = job.finish_time, num_players = job.num_players, \
                num_cpus = job.num_cpus, num_loops = job.num_loops, \
                num_games = job.num_games, sim_dir = job.sim_dir, \
                summary_data = job.summary_data, save_game_data = \
                job.save_game_data)
            finished_job.save()
            
        return Response()
        
class get_finished_job_list(APIView):
    
    def get(self, request):
        finished_job_list = finished_jobs.objects.all()
        finished_job_list = finished_jobs_serializer(finished_job_list, many=True)
        return Response(finished_job_list.data)
        
class put_analyze_job(APIView):
    
    def make_summary_data(self, players1, player_wins, \
        player_hands, card_suits, card_ranks, card_rank_numbers, \
        hand_types, hand_type_ranks, hand_type_wins, hand_type_hands, \
        permutations, hole_hand_wins, hole_hand_hands, hole_hand_tied_wins):
        
        summary_data = {}
        summary_data['players'] = players1    
        summary_data['card_suits'] = card_suits    
        summary_data['card_ranks'] = card_ranks    
        summary_data['card_rank_numbers'] = card_rank_numbers    
        summary_data['hand_types'] = hand_types
        summary_data['hand_type_ranks'] = hand_type_ranks    
        summary_data['permutations'] = permutations
        
        summary_data['total_number_of_games2'] = 0    
        summary_data['player_wins_total'] = player_wins
        summary_data['player_hands_total'] = player_hands
        summary_data['hand_type_wins_total'] = hand_type_wins
        summary_data['hand_type_hands_total'] = hand_type_hands
        summary_data['hole_hand_wins_total'] = hole_hand_wins
        summary_data['hole_hand_tied_wins_total'] = hole_hand_tied_wins
        summary_data['hole_hand_hands_total'] = hole_hand_hands
        summary_data['player_probs'] = {}
        summary_data['hand_type_probs'] = {}
        summary_data['hand_type_probs2'] = {}
        summary_data['hole_hand_probs'] = {}
        summary_data['hole_hand_probs2'] = {}
        summary_data['hole_hand_norm_probs'] = {}
        summary_data['hole_hand_rel_probs'] = {}
        summary_data['hole_hand_rel_probs2'] = {}
        
                
        return summary_data
    
    def initial_summary_data(self, num_players):
        
        players1, player_wins, player_hands = players.get_players()
        card_suits, card_ranks, card_rank_numbers = cards.get_cards()
        hand_types, hand_type_ranks, hand_type_wins, hand_type_hands = \
            hands.get_hands()
        permutations, hole_hand_wins, hole_hand_tied_wins, hole_hand_hands, \
            = hole_hands.get_hole_hands()
        players1, player_wins, player_hands = \
            players.get_game_players(num_players,players1,player_wins, \
            player_hands)
        summary_data = self.make_summary_data(players1, player_wins, \
            player_hands, card_suits, card_ranks, card_rank_numbers, \
            hand_types, hand_type_ranks, hand_type_wins, hand_type_hands, \
            permutations, hole_hand_wins, hole_hand_hands, hole_hand_tied_wins)
        return summary_data
    
    def combine_summary_data(self, finished_job_list, summary_data):
        
        for job in finished_job_list:
            summary_data['total_number_of_games2']= \
                summary_data['total_number_of_games2'] + \
                job.summary_data['total_number_of_games2']
            
            for holeHand in job.summary_data['permutations']:
                summary_data['hole_hand_wins_total'][holeHand] = \
                    summary_data['hole_hand_wins_total'][holeHand] + \
                    job.summary_data['hole_hand_wins_total'][holeHand]
                summary_data['hole_hand_hands_total'][holeHand] = \
                    summary_data['hole_hand_hands_total'][holeHand] + \
                    job.summary_data['hole_hand_hands_total'][holeHand]
                summary_data['hole_hand_tied_wins_total'][holeHand] = \
                    summary_data['hole_hand_tied_wins_total'][holeHand] + \
                    job.summary_data['hole_hand_tied_wins_total'][holeHand]

            for player1 in job.summary_data['player_wins_total'].keys():
                summary_data['player_wins_total'][player1] = \
                    summary_data['player_wins_total'][player1] + \
                    job.summary_data['player_wins_total'][player1]
                summary_data['player_hands_total'][player1] = \
                    summary_data['player_hands_total'][player1] + \
                    job.summary_data['player_hands_total'][player1]
            
            for handType in job.summary_data['hand_types']:
                summary_data['hand_type_wins_total'][handType] = \
                    summary_data['hand_type_wins_total'][handType] + \
                    job.summary_data['hand_type_wins_total'][handType]
                summary_data['hand_type_hands_total'][handType] = \
                    summary_data['hand_type_hands_total'][handType] + \
                    job.summary_data['hand_type_hands_total'][handType]
                
        return summary_data
        
    def putPlayerProbs(self, summary_data):
        
        for player1 in summary_data['player_wins_total'].keys():
            print(player1)
            summary_data['player_probs'][player1] = \
                summary_data['player_wins_total'][player1] / \
                summary_data['total_number_of_games2']  
        return summary_data
        
    def putHandTypeProbs(self, summary_data):
        for handType in summary_data['hand_types']:
            summary_data['hand_type_probs'][handType] = \
                summary_data['hand_type_wins_total'][handType] / \
                summary_data['total_number_of_games2']
    
            if summary_data['hand_type_hands_total'][handType] > 0:
                summary_data['hand_type_probs2'][handType] = \
                    summary_data['hand_type_wins_total'][handType] / \
                    summary_data['hand_type_hands_total'][handType]
            else:
                summary_data['hand_type_probs2'][handType] = 0
        return summary_data       
        
    def putHoleHandProbs(self, summary_data):
        for holeHand in summary_data['permutations']:
            summary_data['hole_hand_probs'][holeHand] = \
                (summary_data['hole_hand_wins_total'][holeHand] \
                    + summary_data['hole_hand_tied_wins_total'][holeHand]) / \
                summary_data['total_number_of_games2']
    
            if summary_data['hole_hand_hands_total'][holeHand] > 0:    
                summary_data['hole_hand_probs2'][holeHand] = \
                    (summary_data['hole_hand_wins_total'][holeHand] + \
                    summary_data['hole_hand_tied_wins_total'][holeHand]) / \
                        summary_data['hole_hand_hands_total'][holeHand]
            else:
                summary_data['hole_hand_probs2'][holeHand] = 0        
    
            if len(holeHand) == 2:
                summary_data['hole_hand_norm_probs'][holeHand] = \
                summary_data['hole_hand_probs'][holeHand]/6
            elif holeHand[2:] == 'S':
                summary_data['hole_hand_norm_probs'][holeHand] = \
                summary_data['hole_hand_probs'][holeHand]/4
            elif holeHand[2:] == 'NS':
                summary_data['hole_hand_norm_probs'][holeHand] = \
                summary_data['hole_hand_probs'][holeHand]/12 
        return summary_data
        
    def getMinNormProb(self, summary_data):
        min_norm_prob_value = np.min(list(summary_data['hole_hand_norm_probs'].values()))
        for name, value in summary_data['hole_hand_norm_probs'].items():
            if value == min_norm_prob_value:
                min_norm_prob_key = name
                break
        return min_norm_prob_key
    
    def putHoleHandRelProbs(self, summary_data):
        for holeHand in summary_data['permutations']:
            minKey = self.getMinNormProb(summary_data)
            if summary_data['hole_hand_norm_probs'][minKey] > 0:    
                summary_data['hole_hand_rel_probs'][holeHand] = \
                    summary_data['hole_hand_norm_probs'][holeHand] / \
                    summary_data['hole_hand_norm_probs'][minKey]
            else:
                summary_data['hole_hand_rel_probs'][holeHand] = 0        

            if summary_data['hole_hand_probs2'][minKey] > 0:    
                summary_data['hole_hand_rel_probs2'][holeHand] = \
                    summary_data['hole_hand_probs2'][holeHand] / \
                    summary_data['hole_hand_probs2'][minKey]    
            else:
                summary_data['hole_hand_rel_probs2'][holeHand] = 0           
        return summary_data
        
    def findLatestJob(self, finished_job_list):
        first_job_name = finished_job_list[0]
        first_job = Simulation_Job.objects.get(job_name=first_job_name)
        max_job_time = first_job.finish_time
        latest_job = first_job
        for i, job_name in enumerate(finished_job_list,1):
            job = Simulation_Job.objects.get(job_name=job_name)
            if (job.finish_time > max_job_time):
                max_job_time = job.finish_time
                latest_job = job
        return latest_job
        
    def getGrandSummaryData(self, latest_job, summary_data):
        grand_total_number_of_games = 0
        for games in latest_job.summary_data['player_wins_grand_total'].values():
            grand_total_number_of_games = grand_total_number_of_games + games
            
        summary_data['grand_total_number_of_games'] = grand_total_number_of_games    
        summary_data['player_wins_grand_total'] = \
            latest_job.summary_data['player_wins_grand_total']
        #summary_data['player_hands_total'] = player_hands_total
        summary_data['player_grand_probs'] = \
            latest_job.summary_data['player_grand_probs']
        summary_data['hand_type_wins_grand_total'] = \
            latest_job.summary_data['hand_type_wins_grand_total']
        summary_data['hand_type_hands_grand_total'] = \
            latest_job.summary_data['hand_type_hands_grand_total']
        summary_data['hand_type_grand_probs'] = \
            latest_job.summary_data['hand_type_grand_probs']
        summary_data['hand_type_grand_probs2'] = \
            latest_job.summary_data['hand_type_grand_probs2']
        summary_data['hole_hand_wins_grand_total'] = \
            latest_job.summary_data['hole_hand_wins_grand_total']
        summary_data['hole_hand_tied_wins_grand_total'] = \
            latest_job.summary_data['hole_hand_tied_wins_grand_total']
        summary_data['hole_hand_hands_grand_total'] = \
            latest_job.summary_data['hole_hand_hands_grand_total']
        summary_data['hole_hand_grand_probs'] = \
            latest_job.summary_data['hole_hand_grand_probs']
        summary_data['hole_hand_grand_probs2'] = \
            latest_job.summary_data['hole_hand_grand_probs2']
        summary_data['hole_hand_norm_grand_probs'] = \
            latest_job.summary_data['hole_hand_norm_grand_probs']
        summary_data['hole_hand_rel_grand_probs'] = \
            latest_job.summary_data['hole_hand_rel_grand_probs']
        summary_data['hole_hand_rel_grand_probs2'] = \
            latest_job.summary_data['hole_hand_rel_grand_probs2']
        return summary_data
    
    def post(self,request):
        analyze_job_list = json.loads(request.POST['analyze_job_list'])
        print(analyze_job_list)
        finished_job_list2 = finished_jobs.objects.all()
        finished_job_list = []
        
        for job in finished_job_list2:   
            if analyze_job_list.__contains__(job.job_name):
                finished_job_list.append(job)
                
        num_players = int(finished_job_list[0].num_players)
        summary_data = self.initial_summary_data(num_players)
        summary_data = self.combine_summary_data(finished_job_list, \
            summary_data)
        summary_data = self.putPlayerProbs(summary_data)
        summary_data = self.putHandTypeProbs(summary_data)
        summary_data = self.putHoleHandProbs(summary_data)
        summary_data = self.putHoleHandRelProbs(summary_data)
        latest_job = self.findLatestJob(analyze_job_list)
        print(latest_job)
        summary_data = self.getGrandSummaryData(latest_job, summary_data)
        
        print(summary_data['player_grand_probs'])
        analyze_job1 = analyzed_jobs(job_name = 'analyze', sim_job_names = \
            json.dumps(analyze_job_list), num_players = str(num_players), \
            summary_data = json.dumps(summary_data), run_time = \
            dt.datetime.now(pytz.utc))          
        analyze_job1.save()
        analyze_job1.job_name = 'analyze' + str(analyze_job1.id)
        analyze_job1.save()
        
        return Response()

class get_analysis_job_list(APIView):

    def get_anal_object(self, status):
        try:
            return analyzed_jobs.objects.filter(status=status)
        except analyzed_jobs.DoesNotExist:
            raise Http404
            
    def get_job_object(self, pk):
        try:
            ds1 = dispatcher_status2.objects.get(pk=pk)
            if ds1.status == 'Reset':
                ds1.status = 'Stopped'
                ds1.job_name = ''
                ds1.save()           
            return ds1
        except:
            ds1 = dispatcher_status2.objects.all().delete()
            ds1 = dispatcher_status2(status = 'Stopped')
            ds1.id = 1
            ds1.save()
            return ds1
            
        
    def get_analyze_job_status_objects(self):
        try:            
            return analyze_job_status.objects.all()
        except:
            raise Http404
    
                 
    def get(self, request):
        
        analyze_job_list = None
        dispatch_status1 = self.get_job_object(pk=1)
        print(dispatch_status1)
        if dispatch_status1.status == 'Stopped':
            analyze_job_list = self.get_anal_object(status = 'pending')
        elif dispatch_status1.status == 'Finished':
            dispatch_status1.status = 'Stopped'
            dispatch_status1.save()
            analyze_job_list = self.get_anal_object(status = 'pending')            
        print(analyze_job_list)      
        analyze_status1 = self.get_analyze_job_status_objects()
        analyze_status1.delete()
        
        analyze_job_list = analyzed_jobs_serializer(analyze_job_list, many = True)
        
        return Response(analyze_job_list.data)        

class start_dispatcher2(APIView):
    
    def get_object(self, pk):
        
        try:
            return dispatcher_status2.objects.get(pk=pk)
        except dispatcher_status2.DoesNotExist:
            raise Http404
    
    def get_first_job_id(self, status):      
        try:
            jobs = analyzed_jobs.objects.filter(status=status)
            min_run_time = jobs[0].run_time
            first_job = jobs[0]
            if jobs.count() > 1:
                for i, job in enumerate(jobs, 1):
                    if job.run_time < min_run_time:
                        min_run_time = job.run_time
                        first_job = job
            return first_job.id
        except:
            raise Http404

    def put_analyze_job_status_objects(self, job_name):
        try:
            aj1 = analyze_job_status(job_name = job_name)
            aj1.save()
            print(aj1)
            return 
        except:
            raise Http404

        
    def start_dispatcher(self):
        
        first_job_id = self.get_first_job_id(status='pending')
        first_job_name = 'analyze' + str(first_job_id)
        print(first_job_name)
        self.put_analyze_job_status_objects(first_job_name)
        args = ['python',  sim_dir + job_script2, str(first_job_id)]
        subprocess.Popen(args, stdout = subprocess.PIPE)
        return
        
    def get(self, request):
        self.start_dispatcher()
        
        dispatcher_status2 =  self.get_object(pk=1)
        if dispatcher_status2.status == 'Finished':
            dispatcher_status2.status = 'Stopped'
            dispatcher_status2.save()
        print('post')
      
        dispatcher_status2 = dispatcher_status_serializer(dispatcher_status2)
        return Response(dispatcher_status2.data)
        
class reset_dispatcher2(APIView):
    
    def set_object(self):
        try:
            ds1 = dispatcher_status2.objects.get(pk=1)
            if ds1.status != 'Reset':
                ds1.status = 'Reset'
                ds1.save()
        except:
            ds1 = dispatcher_status2.objects.all().delete()
            ds1 = dispatcher_status2(status = 'Reset')
            ds1.id = 1
            ds1.save()      
        try:
            sj1 = analyzed_jobs.objects.get(status='running')
            sj1.status ='aborted'
            sj1.save()
        except:
            pass
        return
        
    def get(self,request):
        
        self.set_object()
        return Response("")

class get_dispatcher_status2(APIView):

    def get_object(self, pk):
        try:
            return dispatcher_status2.objects.get(pk=pk)
        except dispatcher_status2.DoesNotExist:
            raise Http404
      
    def get(self,request):
        print(request.GET)
        #status_id = request.GET['dispatcher_status1_id']
        dispatcher_status1 = self.get_object(pk=1)
        serializer = dispatcher_status2_serializer(dispatcher_status1)
        return Response(serializer.data)
        
class get_dispatcher_time2(APIView):
    
    def get_object(self, job_name):
        try:
            return analyzed_jobs.objects.get(job_name=job_name)
        except dispatcher_status.DoesNotExist:
            raise Http404
      
    def post(self,request):
        job_name = request.POST['running_job_name']
        dispatcher_status1 = self.get_object(job_name)
        initial_time = dispatcher_status1.run_time
        current_time = dt.datetime.now(pytz.utc)
        job_time = current_time - initial_time
        hrs = math.floor(job_time.seconds/3600)
        min_secs = job_time.seconds - hrs*3600 
        mins = math.floor(min_secs/60)
        secs = min_secs - mins*60
        time_delta = dt.time(hour=hrs, minute=mins, second=secs)
        dispatcher_time1 = dispatcher_time2(time_delta=time_delta)
        serializer = dispatcher_time2_serializer(dispatcher_time1)
        return Response(serializer.data)
        
class get_analyze_job_status(APIView):
    
    def get_object(self):
        try:
            return analyze_job_status.objects.all()
        except loop_status.DoesNotExist:
            raise Http404
          
    def get(self, request):
        analyze_job_status1 = self.get_object()
        
        serializer = analyze_job_status_serializer(analyze_job_status1, many = True)
        return Response(serializer.data)
        
class get_analyzed_jobs_list(APIView):

    def get(self, request):
        analyzed_jobs_list = analyzed_jobs.objects.all()
        analyzed_jobs_list = analyzed_jobs_serializer(analyzed_jobs_list, many=True)
        return Response(analyzed_jobs_list.data)  
              
class get_analyzed_job_data(APIView):
    
    def get_object(self, analyzed_job_name):
        try:
            return analyzed_jobs.objects.get(job_name = analyzed_job_name)
        except loop_status.DoesNotExist:
            raise Http404
    
    def post(self, request):
        analyzed_job_name = request.POST['analyzed_job_name']
        analyzed_job = self.get_object(analyzed_job_name)
        analyzed_job = analyzed_jobs2_serializer(analyzed_job.data)
        
        return Response(analyzed_job.data)

class initialize_sim(APIView):

    def del_initial_objects(self):
        try:           
            py_scripts1 = python_scripts.objects.all()
            py_scripts1.delete()
            players1 = players.objects.all()
            players1.delete()
            cards1 = cards.objects.all()
            cards1.delete()
            hands1 = hands.objects.all()
            hands1.delete()
            hole_hands1 = hole_hands.objects.all()
            hole_hands1.delete()
            grand_summary = grand_summary_data.objects.all()
            grand_summary.delete()
        except:
            raise Http404
        
    def start_initializer(self):         
        args = ['python',  sim_dir + initial_script]
        subprocess.Popen(args, stdout = subprocess.PIPE)
        return
        
    def get(self, request):
        print("first break")
        self.del_initial_objects() 
        print("second break")
        self.start_initializer()
        print("third break")
        return Response()



class SimStatus(APIView):
    
    def get_object(self, pk):
        try:
            return Simulation_Job.objects.get(pk=pk)
        except Simulation_Job.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        sim_job = self.get_object(pk)
        serializer = Simulation_Job_Serializer(sim_job)
        return Response(serializer.data)
        
    def put(self, request, pk, format = None):
        sim_job = self.get_object(pk)
        serializer = Simulation_Job_Serializer(sim_job, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP400_BAD_REQUEST)
        
    def delete(self, request, pk, format = None):
        sim_job = self.get_object(pk)
        sim_job.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
               
class Finished_Job(APIView):
    def get_object(self, pk):
        try:
            return finished_jobs.objects.get(pk=pk)
        except analyzed_jobs.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        sim_job = self.get_object(pk)
        serializer = finished_jobs_serializer(sim_job)
        return Response(serializer.data)
        
    def put(self, request, pk, format = None):
        sim_job = self.get_object(pk)
        serializer = finished_jobs_serializer(sim_job, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP400_BAD_REQUEST)
        
    def delete(self, request, pk, format = None):
        sim_job = self.get_object(pk)
        sim_job.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
class Analyzed_Job(APIView):
    def get_object(self, pk):
        try:
            return analyzed_jobs.objects.get(pk=pk)
        except analyzed_jobs.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        sim_job = self.get_object(pk)
        serializer = analyzed_jobs_serializer(sim_job)
        return Response(serializer.data)
        
    def put(self, request, pk, format = None):
        sim_job = self.get_object(pk)
        serializer = analyzed_jobs_serializer(sim_job, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP400_BAD_REQUEST)
        
    def delete(self, request, pk, format = None):
        sim_job = self.get_object(pk)
        sim_job.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
                

def details1(request,cpu1loopdata_id):
    return HttpResponse("<h1>Simulation Details Page</h1>"
    "<p> You are looking at Cpu1 record %s Loop Data" % cpu1loopdata_id)
    
def details2(request,cpu2loopdata_id):
    return HttpResponse("<h1>Simulation Details Page</h1>"
    "<p> You are looking at Cpu2 record %s Loop Data" % cpu2loopdata_id)
    
def details3(request,cpu3loopdata_id):
    return HttpResponse("<h1>Simulation Details Page</h1>"
    "<p> You are looking at Cpu2 record %s Loop Data" % cpu3loopdata_id)

