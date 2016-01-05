from django.contrib import admin
from .models import cpu1loopdata, cpu2loopdata, cpu3loopdata

class cpu1loopdataAdmin(admin.ModelAdmin):
    fieldsets = [
        ( None, {'fields': ['run_time', 'num_players', 'cpu_num']}),
        ('Non Tied Hands', {'fields': ['non_tied_hands'],
                        'classes': ['collapse']}),
 
        ('Tied Hands', {'fields': ['tied_hands'],
                        'classes': ['collapse']}),

        ('Parent Data', {'fields': ['parent_data'],
                        'classes': ['collapse']}),
         ]
         
         
    list_display = ('run_time', 'num_players', 'cpu_num')
    list_filter = ['run_time'] 
    
class cpu2loopdataAdmin(admin.ModelAdmin):
    fieldsets = [
        ( None, {'fields': ['run_time', 'num_players', 'cpu_num']}),
         
        ('Non Tied Hands', {'fields': ['non_tied_hands'],
                        'classes': ['collapse']}),
 
        ('Tied Hands', {'fields': ['tied_hands'],
                        'classes': ['collapse']}),

        ('Parent Data', {'fields': ['parent_data'],
                        'classes': ['collapse']}),

         ]
    
    list_display = ('run_time', 'num_players', 'cpu_num')
    list_filter = ['run_time']     


class cpu3loopdataAdmin(admin.ModelAdmin):
    fieldsets = [
        ( None, {'fields': ['run_time', 'num_players', 'cpu_num']}),
         
        ('Non Tied Hands', {'fields': ['non_tied_hands'],
                        'classes': ['collapse']}),
 
        ('Tied Hands', {'fields': ['tied_hands'],
                        'classes': ['collapse']}),

        ('Parent Data', {'fields': ['parent_data'],
                        'classes': ['collapse']}),
         ]

    list_display = ('run_time', 'num_players', 'cpu_num')
    list_filter = ['run_time']     
         
# Register your models here.
admin.site.register(cpu1loopdata, cpu1loopdataAdmin)
admin.site.register(cpu2loopdata, cpu2loopdataAdmin)
admin.site.register(cpu3loopdata, cpu3loopdataAdmin)

