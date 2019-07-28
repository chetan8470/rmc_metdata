"""rmc_metdata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from state import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$',views.home),
	url(r'^station_temperature_form/',views.station_temperature_form),
	url(r'^form_submit/', views.form_submit),
	url(r'^accounts/', include('django.contrib.auth.urls')),
	url(r'^logout/', views.logout_view),
	
	url(r'^delhi/',views.delhi),
	url(r'^delhi_display_data/', views.delhi_display_data),
	
	url(r'^haryana/',views.haryana),
	url(r'^haryana_display_data/', views.haryana_display_data),
	
	url(r'^jk/',views.jk),
	url(r'^jk_display_data/', views.jk_display_data),
	
	url(r'^hp/',views.hp),
	url(r'^hp_display_data/', views.hp_display_data),
	
	url(r'^uk/',views.uk),
	url(r'^uk_display_data/', views.uk_display_data),
	
	url(r'^punjab/',views.punjab),
	url(r'^punjab_display_data/', views.punjab_display_data),
	
	url(r'^rajasthan_east/',views.rajasthan_east),
	url(r'^rajasthan_east_display_data/', views.rajasthan_east_display_data),
	
	url(r'^rajasthan_west/',views.rajasthan_west),
	url(r'^rajasthan_west_display_data/', views.rajasthan_west_display_data),
	
	url(r'^up_east/',views.up_east),
	url(r'^up_east_display_data/', views.up_east_display_data),
	
	url(r'^up_west/',views.up_west),
	url(r'^up_west_display_data/', views.up_west_display_data),
	
	
	
	url(r'^display_data_annually/', views.display_data_annually),
	url(r'^display_data_monthly/', views.display_data_monthly),
	url(r'^display_data_daily/', views.display_data_daily),
	url(r'^display_data_records_all_stations_particular_date/', views.display_data_records_all_stations_particular_date),
	url(r'^display_data_date_specification_duration/', views.display_data_date_specification_duration),
	
	url(r'^display_data_annually_result/', views.display_data_annually_result),
	url(r'^display_data_monthly_result/', views.display_data_monthly_result),
	url(r'^display_data_daily_result/', views.display_data_daily_result),
	url(r'^display_data_records_all_stations_particular_date_result/', views.display_data_records_all_stations_particular_date_result),
	url(r'^display_data_date_specification_duration_result/', views.display_data_date_specification_duration_result),

	
	#url(r'^csv_download/', views.getfile_annually),
	
	
	
]
