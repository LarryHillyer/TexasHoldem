# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 18:56:17 2015

@author: Larry
"""

#from django import forms
from django.forms import ModelForm
from .models import Simulation_Job, dispatcher_status, dispatcher_status2
#from functools import partial

PLAYER_CHOICES = (('2','2 Players'), ('3','3 Players'), ('4','4 Players'), \
    ('5','5 Players'), ('6','6 Players'), ('7','7 Players'), ('8','8 Players'))

#DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class Simulation_Job_Form1(ModelForm):
    class Meta:
        model = Simulation_Job
        fields = ['num_players', 'num_cpus','num_loops', \
            'num_games','sim_dir', 'save_game_data']

class Simulation_Job_Form2(ModelForm):
    class Meta:
        model = Simulation_Job
        fields = []
        
class Simulation_Job_Form3(ModelForm):
    class Meta:
        model = Simulation_Job
        fields = ['num_players','run_time']

class dispatcher_status_form(ModelForm):
    class Meta:
        model = dispatcher_status
        fields = []

class dispatcher_status2_form(ModelForm):
    class Meta:
        model = dispatcher_status2
        fields = []

        
"""                
class query_jobs_form(forms.Form):
    
    num_players = forms.CharField(label = 'num_players', max_length = 2, \
        widget = forms.Select(choices = PLAYER_CHOICES,))
        
    start_date = forms.DateField(widget = forms.DateInput())
    end_date = forms.DateField(widget = forms.DateInput())



CPU_CHOICES = (('1', '1'), ('2','2'), ('3','3'))


class Simulation_Job_Form2(forms.Form):
    
    job_name = forms.CharField(label = 'job_name', max_length = 50)
    
    num_players = forms.CharField(label = 'num_players', max_length = 2, \
        widget = forms.Select(choices = PLAYER_CHOICES,))
    
    num_cpus = forms.CharField(label = 'num_cpus', max_length = 2, \
        widget = forms.Select(choices = CPU_CHOICES))
    
    num_loops = forms.CharField(label = 'num_loops', max_length = 3)
    num_games = forms.CharField(label = 'num_games', max_length = 12)
"""
      

            
        