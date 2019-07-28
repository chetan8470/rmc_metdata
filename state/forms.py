from django import forms

state_id = {
		'jammu and kashmir':1,
		'himachal pradesh':2,
		'uttarakhand':3,
		'punjab':4,
		'haryana':5,
		'delhi':6,
		'east uttar pradesh': 7,
		'west uttar pradesh':8,
		'east rajasthan':9,
		'west rajasthan':10
	}
	
station_id = {
		'Srinagar':101,
		'Qazigund':102,
		'Pahalgam':103,
		'Kupwara':104,
		'Kukernag':105,
		'Gulmarg':106,
		'Jammu':107,
		'Banihal':108,
		'Batote':109,
		'Katra':110,
		'Bhaderwah':111,
		
		'Bhuntar':201,
		'Bilaspur':202,
		'Chamba':203,
		'Dalhousie':204,
		'Dharamshala':205,
		'Hamirpur':206,
		'Kalpa':207,
		'Kangra':208,
		'Keylong':209,
		'Manali':210,
		'Mandi':211,
		'Nahan':212,
		'Palampur':213,
		'Shimla':214,
		'Solan':215,
		'Sundernagar':2016,
		'Una':217,
		
		'Dehradun':301,
		'Pantnagar':302,
		'Mukteshwar':303,
		'Tehri':304,
		'Pithoragarh':305,
		'Nainital':306,
		'Mussoorie':307,
		'Jollygrant':308,
		'Roorkee':309,
		'Joshimath':310,
		'DhanauriHaridwar':311,
		'Munsyari':312,
		'Tiuni':313,
		'Ghansali':314,
		'Matela Almora':315,
		'Ranichawri':316,
		'Gairsain':317,
		'Chamoli':318,
		'Rudraprayag':319,
		'Uttarkashi':320,
		
		'AMRITSAR':401,
		'LUDHIANA':402,
		'PATIALA':403,
		'PATHANKOTIAF':404,
		'AdampurIAF':405,
		'HalwaraIAF':406,
		'BathindaIAF':407,
		'BathindaAMFU':408,
		'FaridkotAMFU':409,
		'GurdaspurAMFU':410,
		'Ballowal Saunkhri':411,
		
		'Chandigarh':501,
		'Chandigarh(IAF)':502,
		'Ambala':503,
		'Hisar':504,
		'Karnal':505,
		'Narnaul':506,
		'Rohtak':507,
		
		'Safdarjung':601,
		'Palam':602,
		'Lodhi Road':603,
		'Delhi Ridge':604,
		'Ayanagar':605,
		
		'Lucknow':701,
		'Barabanki':702,
		'HardoiOB':703,
		'KanpurIAF':704,
		'Kanpurcity':705,
		'EtawahOB':706,
		'L.Kheri':707,
		'Gorakhpur':708,
		'Varanasi AP':709,
		'Varanasi BHU':710,
		'Ballia':711,
		'Churk':712,
		'Bahraich':713,
		'Allahabad':714,
		'Banda':715,
		'Sultanpur Ob':716 ,
		'Fursatganj Ob.':717 ,
		'Ghazipur':718,
		
		'Jhansi':801,
		'Orai':802,
		'Hamirpur':803,
		'Fatehgarh':804,
		'Bareilly Ob.':805,
		'Shahajhanpur P/T':806,
		'Najibabad P/T':807,
		'Moradabad P/T':808,
		'Muzaffarnagar P/T':809,
		'Meerut':810,
		'Agra':811,
		'Aligarh':812,
		
		'Ajmer':901,
		'Bhilwara':902,
		'Vanasthali':903,
		'Alwar':904,
		'Jaipur':905,
		'Pilani':906,
		'Sikar':907,
		'Kota':908,
		'S.madhopur':909,
		'Bundi':910,
		'Chittorgarh':911,
		'Dabok':912,
		'Mt. Abu':913,
		
		'Barmer':1001,
		'Er. Road':1002,
		'Jaisalmer':1003,
		'Jalore':1004,
		'Jodhpur City':1005,
		'Phalodi':1006,
		'Bikaner':1007,
		'Churu':1008,
		'Ganganagar':1009,
	}


state = (
		('jammu and kashmir','JAMMU AND KASHMIR'),
		('himachal pradesh','HIMACHAL PRADESH'),
		('uttarakhand','UTTARAKHAND'),
		('punjab','PUNJAB'),
		('haryana','HARYANA'),
		('delhi','DELHI'),
		('east uttar pradesh',' EAST UTTAR PRADESH'),
		('west uttar pradesh','WEST UTTAR PRADESH'),
		('east rajasthan','EAST RAJASTHAN'),
		('west rajasthan','WEST RAJASTHAN')
	)
	
station = (
		('Srinagar','SRINAGAR'),
		('Qazigund','QAZIGUND'),
		('Pahalgam','PAHALGAM'),
		('Kupwara','KUPWARA'),
		('Kukernag','KUKERNAG'),
		('Gulmarg','GULMARG'),
		('Jammu','JAMMU'),
		('Banihal','BANIHAL'),
		('Batote','BATOTE'),
		('Katra','KATRA'),
		('Bhaderwah','BHADERWAH'),
		('Bhuntar','BHUNTAR'),
		('Bilaspur','BILASPUR'),
		('Chamba','CHAMBA'),
		('Dalhousie','DALHOUSIE'),
		('Dharamshala','DHARAMSHALA'),
		('Hamirpur','HAMIRPUR'),
		('Kalpa','KALPA'),
		('Kangra','KANGRA'),
		('Keylong','KEYLONG'),
		('Manali','MANALI'),
		('Mandi','MANDI'),
		('Nahan','NAHAN'),
		('Palampur','PALAMPUR'),
		('Shimla','SHIMLA'),
		('Solan','SOLAN'),
		('Sundernagar','SUNDERNAGAR'),
		('Una','UNA'),
		('Dehradun','DEHRADUN'),
		('Pantnagar','PANTNAGAR'),
		('Mukteshwar','MUKTESHWAR'),
		('Tehri','TEHRI'),
		('Pithoragarh','PITHORAGARH'),
		('Nainital','NAINITAL'),
		('Mussoorie','MUSSOORIE'),
		('Jollygrant','JOLLYGRANT'),
		('Roorkee','ROORKEE'),
		('Joshimath','JOSHIMATH'),
		('Dhanauri(Haridwar)','DHANAURI (HARIDWAR)'),
		('Munsyari','MUNSYARI'),
		('Tiuni','TIUNI'),
		('Ghansali','GHANSALI'),
		('Matela (Almora)','MATELA (ALMORA)'),
		('Ranichawri','RANICHAWRI'),
		('Gairsain','GAIRSAIN'),
		('Chamoli','CHAMOLI'),
		('Rudraprayag','RUDRAPRAYAG'),
		('Uttarkashi','UTTARKASHI'),
		('AMRITSAR','AMRITSAR'),
		('LUDHIANA','LUDHIANA'),
		('PATIALA','PATIALA'),
		('PATHANKOT(IAF)','PATHANKOT(IAF)'),
		('Adampur(IAF)','ADAMPUR(IAF)'),
		('Halwara(IAF)','HALWARA(IAF)'),
		('Bathinda(IAF)','BATHINDA(IAF)'),
		('Bathinda(AMFU)','BATHINDA(AMFU)'),
		('Faridkot(AMFU)','FARIDKOT (AMFU)'),
		('Gurdaspur(AMFU)','GURDASPUR (AMFU)'),
		('Ballowal Saunkhri','BALLOWAL SAUNKHRI'),
		('Chandigarh','CHANDIGARH'),
		('Chandigarh(IAF)','CHANDIGARH (IAF)'),
		('Ambala','AMBALA'),
		('Hisar','HISAR'),
		('Karnal','KARNAL'),
		('Narnaul','NARNAUL'),
		('Rohtak','ROHTAK'),
		('Safdarjung','SAFDARJUNG'),
		('Palam','PALAM'),
		('Lodhi Road','LODHI ROAD'),
		('Delhi Ridge','DELHI RIDGE'),
		('Ayanagar','AYANAGAR'),
		('Lucknow','LUCKNOW'),
		('Barabanki','BARABANKI'),
		('Hardoi(OB)','HARDOI(OB)'),
		('Kanpur(IAF)','KANPUR(IAF)'),
		('Kanpur(city)','KANPUR(CITY)'),
		('Etawah(OB)','ETAWAH(OB)'),
		('L.Kheri','L.KHERI'),
		('Gorakhpur','GORAKHPUR'),
		('Varanasi AP','VARANASI AP'),
		('Varanasi BHU','VARANASI BHU'),
		('Ballia','BALLIA'),
		('Churk','CHURK'),
		('Bahraich','BAHRAICH'),
		('Allahabad','ALLAHABAD'),
		('Banda','BANDA'),
		('Sultanpur Ob','SULTANPUR OB.'),
		('Fursatganj Ob.','FURSATGANJ OB.'),
		('Ghazipur','GHAZIPUR'),
		('Jhansi','JHANSI'),
		('Orai','ORAI'),
		('Hamirpur','HAMIRPUR'),
		('Fatehgarh','FATEHGARH'),
		('Bareilly Ob.','BAREILLY OB.'),
		('Shahajhanpur P/T','SHAHAJHANPUR P/T'),
		('Najibabad P/T','NAJIBABAD P/T'),
		('Moradabad P/T','MORADABAD P/T'),
		('Muzaffarnagar P/T','MUZAFFARNAGAR P/T'),
		('Meerut','MEERUT'),
		('Agra','AGRA'),
		('Aligarh','ALIGARH'),
		('Ajmer','AJMER'),
		('Bhilwara','BHILWARA'),
		('Vanasthali','VANASTHALI'),
		('Alwar','ALWAR'),
		('Jaipur','JAIPUR'),
		('Pilani','PILANI'),
		('Sikar','SIKAR'),
		('Kota','KOTA'),
		('S.madhopur','S.MADHOPUR'),
		('Bundi','BUNDI'),
		('Chittorgarh','CHITTORGARH'),
		('Dabok','DABOK'),
		('Mt. Abu','MT. ABU'),
		('Barmer','BARMER'),
		('Er. Road','ER. ROAD'),
		('Jaisalmer','JAISALMER'),
		('Jalore','JALORE'),
		('Jodhpur City','JODHPUR CITY'),
		('Phalodi','PHALODI'),
		('Bikaner','BIKANER'),
		('Churu','CHURU'),
		('Ganganagar','GANGANAGAR'),
	)

from state.models import station_temperature_data
class station_temperature_data_form(forms.ModelForm) :
	class Meta :
		model = station_temperature_data
		fields = '__all__'

	def clean(self) :
		total_cleaned_data = super().clean()
		inputstate = total_cleaned_data['state']
		inputstate_id = total_cleaned_data['state_id']
		print('state = ',inputstate,'state id = ',inputstate_id)
		inputstation = total_cleaned_data['station']
		inputstation_id = total_cleaned_data['station_id']
		print('station = ',inputstation,'station id = ',inputstation_id)
		
		if state_id[inputstate] != inputstate_id :
			raise forms.ValidationError('State id and State name are not same')

		if station_id[inputstation] != inputstation_id :
			raise forms.ValidationError('Station id and Station name are not same')
		
		
		
		
class display_data_annually_form(forms.Form) :
	station = forms.CharField(widget=forms.Select(choices=station))
	year = forms.IntegerField()
	
class display_data_monthly_form(forms.Form) :
	station = forms.CharField(widget=forms.Select(choices=station))
	year = forms.IntegerField()
	month = forms.IntegerField()
	
class display_data_daily_form(forms.Form) :
	state = forms.CharField(widget=forms.Select(choices=state))
	year = forms.IntegerField()
	month = forms.IntegerField()
	date = forms.IntegerField()
	
class display_data_records_all_stations_particular_date_form(forms.Form) :
	#station = forms.CharField(widget=forms.Select(choices=station))
	year = forms.IntegerField()
	month = forms.IntegerField()
	date = forms.IntegerField()
	
class display_data_date_specification_duration_form(forms.Form) :
	station = forms.CharField(widget=forms.Select(choices=station))
	fromdate = forms.DateField()
	todate = forms.DateField()
	def clean(self) :
		total_cleaned_data = super().clean()
		inputfromdate = total_cleaned_data['fromdate']
		inputtodate = total_cleaned_data['todate']
		if inputfromdate.input_formats == [ '%Y-%m-%d' ] :
			raise forms.ValidationError('Your Start date formate is not same assSpecified')
		if inputtodate.input_formats == [ '%Y-%m-%d' ] :
			raise forms.ValidationError('Your end date formate is not same assSpecified')

class display_data_annually_result_form(forms.Form) :
	station = forms.CharField(required=False,widget=forms.HiddenInput)
	year = forms.IntegerField(required=False,widget=forms.HiddenInput)
	















