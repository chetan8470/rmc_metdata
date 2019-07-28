from django.contrib import admin
from state.models import station_temperature_data

# Register your models here.

class station_temperature_dataAdmin(admin.ModelAdmin) :
	list_display = [	
		'state_id','state','station_id','station','date',
		'Maximum_temperature','Maximum_temperature_previous',
		'Maximum_normal','Maximum_change','Maximum_departure',
		'Minimum_temperature','Minimum_temperature_previous',
		'Minimum_normal','Minimum_change','Minimum_departure',
		'rainfall'
		]

admin.site.register(station_temperature_data,station_temperature_dataAdmin)