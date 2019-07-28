from django.db import models
import datetime

# Create your models here.

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


class station_temperature_data(models.Model) :
	state_id = models.IntegerField(default=0,editable=True)
	state = models.CharField(max_length = 100,choices=state)
	station_id = models.IntegerField(editable=True)
	station = models.CharField(max_length = 100,choices=station)
	date = models.DateField(auto_now_add=False)
	Maximum_temperature = models.FloatField()
	Maximum_temperature_previous = models.FloatField()
	Maximum_normal = models.FloatField()
	Maximum_change = models.FloatField()
	Maximum_departure = models.FloatField()
	Minimum_temperature = models.FloatField()
	Minimum_temperature_previous = models.FloatField()
	Minimum_normal = models.FloatField()
	Minimum_change = models.FloatField()
	Minimum_departure = models.FloatField()
	rainfall = models.FloatField()


