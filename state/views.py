from django.shortcuts import render
from . import forms
from django.contrib.auth.decorators import login_required
from state.models import *
# Create your views here.
from django.http import *
import csv 

#test

def home(request) :
	return render(request,'state/home.html')
	
@login_required	
def station_temperature_form(request) :
	form = forms.station_temperature_data_form()
	if request.method == 'POST' :
		form = forms.station_temperature_data_form(request.POST)
		if form.is_valid() :
			print('form run suceessfully')
			form.save(commit = True)
			return render(request,'state/form_submit.html')
		else :	
			return render(request,'state/station_temperature_form.html',{'form':form})
	return render(request,'state/station_temperature_form.html',{'form':form})
	
def form_submit(request) :
	return render(request,'state/form_submit.html')
	
def logout_view(request) :
	pass
	
	
	
def delhi(request) :
	return render(request,'state/delhi.html')
	
def haryana(request) :
	return render(request,'state/haryana.html')
	
def jk(request) :
	return render(request,'state/j&k.html')
	
def hp(request) :
	return render(request,'state/hp.html')
	
def uk(request) :
	return render(request,'state/uk.html')
	
def rajasthan_east(request) :
	return render(request,'state/rajasthan_east.html')
	
def punjab(request) :
	return render(request,'state/punjab.html')
	
def rajasthan_west(request) :
	return render(request,'state/rajasthan_west.html')
	
def up_east(request) :
	return render(request,'state/up_east.html')
	
def up_west(request) :
	return render(request,'state/up_west.html')
	
	
	
	
def delhi_display_data(request) :
	return render(request,'state/delhi_display_data.html')
	
def haryana_display_data(request) :
	return render(request,'state/haryana_display_data.html')
	
def jk_display_data(request) :
	return render(request,'state/j&k_display_data.html')
	
def hp_display_data(request) :
	return render(request,'state/hp_display_data.html')
	
def uk_display_data(request) :
	return render(request,'state/uk_display_data.html')
	
def punjab_display_data(request) :
	return render(request,'state/punjab_display_data.html')
	
def rajasthan_east_display_data(request) :
	return render(request,'state/rajasthan_east_display_data.html')
	
def rajasthan_west_display_data(request) :
	return render(request,'state/rajasthan_west_display_data.html')
	
def up_east_display_data(request) :
	return render(request,'state/up_east_display_data.html')
	
def up_west_display_data(request) :
	return render(request,'state/up_west_display_data.html')
		
		
		
	
def display_data_annually(request):
	form = forms.display_data_annually_form()
	if request.method == 'POST' :
		form = forms.display_data_annually_form(request.POST)
		if form.is_valid() :
			return render(request,'state/display_data_annually_result.html')
	return render(request,'state/display_data_annually.html',{'form':form})
	

def display_data_annually_result(request):
	result1 = station_temperature_data.objects.filter(station__exact = request.POST['station']).filter(date__year=request.POST['year'])
	return render(request,'state/display_data_annually_result.html',{'result':result1})
	
def display_data_monthly(request):
	form = forms.display_data_monthly_form()
	if request.method == 'POST' :
		form = forms.display_data_monthly_form(request.POST)
		if form.is_valid() :
			return render(request,'state/display_data_monthly_result.html')
	return render(request,'state/display_data_monthly.html',{'form':form})
	

def display_data_monthly_result(request):
	result = station_temperature_data.objects.filter(station__exact = request.POST['station']).filter(date__year=request.POST['year']).filter(date__month=request.POST['month'])
	return render(request,'state/display_data_monthly_result.html',{'result':result})


def display_data_daily(request):
	form = forms.display_data_daily_form()
	if request.method == 'POST' :
		form = forms.display_data_daily_form(request.POST)
		if form.is_valid() :
			return render(request,'state/display_data_daily_result.html')
	return render(request,'state/display_data_daily.html',{'form':form})

def display_data_daily_result(request):
	result = station_temperature_data.objects.filter(date__year=request.POST['year']).filter(date__month=request.POST['month']).filter(date__day=request.POST['date'])
	return render(request,'state/display_data_daily_result.html',{'result':result})

def display_data_records_all_stations_particular_date(request):
	form = forms.display_data_records_all_stations_particular_date_form()
	if request.method == 'POST' :
		form = forms.display_data_records_all_stations_particular_date_form(request.POST)
		if form.is_valid() :
			return render(request,'state/display_data_records_all_stations_particular_date_form.html')
	return render(request,'state/display_data_records_all_stations_particular_date.html',{'form':form})



def display_data_records_all_stations_particular_date_result(request):
	response = HttpResponse(content_type='text/csv')  
	response['Content-Disposition'] = 'attachment; filename="station_temperature_data.csv"' 
	result = station_temperature_data.objects.filter(date__year=request.POST['year']).filter(date__month=request.POST['month']).filter(date__day=request.POST['date'])
	writer = csv.writer(response) 
	writer.writerow([	
		'state_id','state','station_id','station','date',
		'Maximum_temperature','Maximum_temperature_previous',
		'Maximum_normal','Maximum_change','Maximum_departure',
		'Minimum_temperature','Minimum_temperature_previous',
		'Minimum_normal','Minimum_change','Minimum_departure',
		'rainfall'
		])
	for s in result:  		
		writer.writerow([s.state_id,s.state,s.station_id,s.station,s.date,s.Maximum_temperature,s.Maximum_temperature_previous,s.Maximum_normal,s.Maximum_change,s.Maximum_departure,s.Minimum_temperature,s.Minimum_temperature_previous,s.Minimum_normal,s.Minimum_change,s.Minimum_departure,s.rainfall]) 
	return response	
	

def display_data_date_specification_duration(request):
	form = forms.display_data_date_specification_duration_form()
	if request.method == 'POST' :
		form = forms.display_data_date_specification_duration_form(request.POST)
		if form.is_valid() :
			return render(request,'state/display_data_date_specification_duration_form.html')
	return render(request,'state/display_data_date_specification_duration.html',{'form':form})



def display_data_date_specification_duration_result(request):
	result = station_temperature_data.objects.filter(station__exact = request.POST['station']).filter(date__range=(request.POST['fromdate'], request.POST['todate']))
	return render(request,'state/display_data_date_specification_duration_result.html',{'result':result})



	
	
	
 
 
	
	
	
    
 
	
	
	
	
	
	
	
	
	
	
	
	
	
	