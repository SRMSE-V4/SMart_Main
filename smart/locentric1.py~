import cgitb
cgitb.enable()
import math
from pymongo import MongoClient

loc = {
    'pune' : [18.53,73.85],
    'nashik' : [20.02,73.5],
    'miraj' : [16.83,74.63],
    'aurangabad' : [19.78,75.29],
    'mumbai' : [18.97,72.85],
    'nagpur' : [21.07,79.27],
    'satara' : [17.69,73.85],
    'latur' : [18.24,76.82],
    'miraj' : [16.83,74.63],
    'parbhani' : [19.27,76.78],
    'pimpri' : [],
    'chinchwad' : [18.37,73.48],
    'dhule' : [20.9,74.78],
    'kolhapur' : [16.7,74.23],
    'sangli' : [16.87,74.57],
    'beed' : [18.99,75.76],
    'malegaon' : [20.55,74.55],
    'ahmednagar' : [19.08,74.73],
    'shirdi' : [19.77,74.78],
    'solapur' : [17.68,75.92],
    'jalgaon' : [21.02,75.57],
    'nanded' : [19.09,77.27],
    'amravati' : [20.93,77.75],
    'osmanabad' : [18.17,76.05],
    'ratnagiri' : [16.98,73.3],
    'athani' : [16.73,75.07],
    'vashi' : [19.08,73.01],
    'shirur' : [18.83,74.38],
    'jaina' : [19.83,75.88],
    'ausa' : [18.25,76.5],
    'powai' : [19.12,72.91], 
    'nerul' : [19.02,73.02],  
    'mulund' : [19.17,72.96],  
    'thane' : [19.17,72.96],  
    'akola' : [20.7,77],  
    'dombivali' : [19.22,73.09], 
    'lucknow' : [26.85,80.92],  
    'noida' : [28.57,77.32],  
    'agra' : [27.18,78.02],  
    'dadri' : [28.57,77.55],  
    'kanpur' : [26.46,80.33],  
    'bahraich' : [27.58,81.6],  
    'allahabad' : [25.45,81.85],  
    'ghaziabad' : [28.67,77.42], 
    'bareilly' : [28.55,80.12],  
    'etawah' : [26.77,79.03],  
    'modinagar' : [28.91,77.63],  
    'jaunpur' : [25.73,82.68],
    'hyderabad' : [17.01,78.84], 
    'visakhapatnam' : [17.7,83.25],  
    'gokavaram' : [17.27,81.85],  
    'kotanandur' : [17.47,82.47],  
    'kadapa' : [14.47,78.92],  
    'kurnool' : [15.83,78.05],  
    'secunderabad' : [17.45,78.5], 
    'warangal' : [18,79.6],
    'somajiguda' : [17.43,78.46],
    'nawada' : [24.88,85.53],
    'patna' : [25.61,85.14],
    'mysore' : [12.3,76.65],
    'bellary' : [12.3,76.65],
    'gulbarga' : [17.33,76.83],
    'hassan' : [13.06,76.1],
    'gadag' : [15.43,75.63],
    'hubli' : [15.3617,75.0849],
    'bangalore' : [12.97,77.57],
    'mandya' : [12.52,76.9],
    'udupi' : [13.59,74.75],
    'davanagere' : [14.47,75.92],
    'bijapur' : [16.82,75.72],
    'bagalkot' : [16.1817,75.6958],
    'indi' : [17.17,75.97],
    'belgaum' : [15.85,74.55],
    'mangalore' : [12.87,74.88],
    'manipal' : [13.35,74.78],
    'kolar' : [13.13,78.13],
    'belgaum' : [15.85,74.55],
    'chikkaballapur' : [13.43,77.42],
    'bhatkal' : [13.97,],
    'sirsi' : [14.6195,74.8354],
    'bidar' : [17.9,77.53],
    'chamarajanagar' : [11.93,76.94],
    'allapuzha' : [9.49,76.33],
    'pathanamthitta' : [9.27,76.78],
    'thiruvananthapuram' : [8.49,76.95],
    'kottayam' : [9.58,76.52],
    'malappuram' : [11.04,76.08],
    'thrissur' : [10.52,76.21],
    'thiruvalla' : [9.39,76.58],
    'kozhikode' : [11.25,75.77],
    'manarkadu' : [9.61,76.58],
    'kochi' : [9.98,76.27],
    'muvattupuzha' : [9.97,76.58],
    'ernakulam' : [9.98,76.28],
    'angamaly' : [10.2,76.4],
    'ahmedabad ' : [23.03,72.58],
    'rajkot' : [ 22.3,70.78],
    'vadodara' : [22.3,73.2],
    'surat' : [21.17,72.83],
    'bhavnagar' : [21.76,72.15],
    'jamnagar' : [22.47,70.07],
    'bhuj' : [23.27,69.67],
    'gandhidham' : [23.03,70.13],
    'una' : [20.82,71.03],
    'junagadh' : [21.52,70.47],
    'porbandar' : [21.63,69.6],
    'amreli' : [21.62,71.23],
    'godhra' : [22.77,73.72],
    'delhi' : [28.61,77.23],
    'mandi' : [31.72,76.92],
    'baddi' : [30.94,76.78],
    'hamirpur' : [31.68,76.52],
    'una' : [31.48,76.28],
    'nahan' : [30.55,77.3],
    'paonta sahib' : [30.45,77.62],
    'shimla' : [31.1,77.17],
    'chaupal' : [30.95,77.58],
    'barotiwala' : [30.92,77.12],
    'kangra' : [32.22,76.3],
    'tanda' : [32.1,76.3],
    'manali' : [32.27,77.27],
    'chennai' : [13.09,80.27],
    'vellore' : [12.87,79.12],
    'coimbatore' : [11.02,76.97],
    'nagercoil' : [8.17,77.43],
    'madurai' : [9.13,78.17],
    'acharipallam' : [8.17,77.4],
    'kanyakumari' : [8.08,77.54],
    'thanjavur' : [10.8,79.15],
    'tirunelveli' : [8.73,77.7],
    'panjim' : [15.48,73.83],
    'margao' : [15.3,73.83],
    'panaji' : [15.3,73.95],
    'bambolim' : [15.48,73.83],
    'harda' : [22.33,77.1],
    'bhopal' : [23.25,77.42],
    'indore' : [22.42,75.54],
    'jabalpur' : [23.16,79.94],
    'gwalior' : [26.14,78.1],
    'chhindwara' : [22.07,78.93],
    'guna' : [24.65,77.32],
    'gangapur' : [26.47,76.72],
    'jodhpur' : [26.28,73.02],
    'barmer' : [25.75,71.38],
    'kota' : [25.18,75.83],
    'bhilawara' : [25.35,74.63],
    'udaipur' : [24.58,73.68],
    'kishangarh' : [26.57,74.87],
    'nagaur' : [27.2,73.73],
    'pratapgarh' : [24.03,74.78],
    'rajsamand' : [25.07,73.88],
    'ajmer' : [26.27,74.42],
    'jaipur' : [26.93,75.82],
    'alwar' : [27.34,76.38],
    'hanumangarh' : [29.58,74.32],
    'pali' : [24.48,78.42],
    'jhunjhunu' : [28.13,75.4],
    'bundi' : [25.44,75.64],
    'chittorgarh' : [24.88,74.63],
    'sirohi' : [24.89,72.86],
    'banswara' : [23.55,74.45],
    'bharatpur' : [27.22,77.48],
    'churu' : [28.3,74.95],
    'dausa' : [26.88,76.33],
    'karauli' : [26.5,77.02],
    'zirakpur' : [30.65,76.82],
    'jalandhar' : [31.33,75.58],
    'amritsar' : [31.64,74.86],
    'samrala' : [30.84,76.19],
    'nabha' : [30.37,76.15],
    'bathinda' : [30.23,74.95],
    'mohali' : [30.78,76.69],
    'faridkot' : [30.67,74.75],
    'moga' : [30.8,75.17],
    'lalru' : [30.29,76.48],
    'kharar' : [30.74,76.65],
    'ludhiana' : [30.91,75.85],
    'ferozepur' : [30.92,74.6],
    'patiala' : [30.33,76.4],
    'mandi Gobindgarh' : [30.41,76.18],
    'longowal' : [30.22,75.68],
    'pathankot' : [32.27,75.65],
    'phagwara' : [31.22,75.77],
    'khanna' : [30.7,76.22],
    'hoshiarpur' : [31.53,75.92],
    'ropar' : [31.2,76.6],
    'puducherry' : [11.93,79.83],
    'chandigarh' : [30.75,76.78],
    'jagadhri' : [30.17,77.3],
    'pinjore' : [30.8,76.92],
    'panchkula' : [30.74,76.8],
    'kurukshetra' : [30,76.45],
    'gurgaon' : [28.47,77.03],
    'ambala' : [30.38,76.78],
    'faridabad' : [28.42,77.31],
    'sirsa' : [29.53,75.02],
    'rohtak' : [28.9,76.57],
    'jakhal Mandi' : [29.8,75.83],
    'yamunanagar' : [30.1,77.28],
    'kaithal' : [29.8,76.38],
    'fatehabad' : [29.52,75.45],
    'nahan' : [30.55,77.3],
    'dehradun' : [30.33,78.06],
    'cuttack' : [20.27,85.52],
    'bhubaneswar' : [20.27,85.84],
    'burla' : [21.5,83.87],
    'ranchi' : [23.35,85.33],
    'rourkela' : [22.12,84.54],
    'binjharpur' : [20.85,86.33],
    'jammu' : [32.73,32.73],
    'nowshera' : [34,72],
    'srinagar' : [34.09,74.79],
    'guwahati' : [26.17,91.77],
    'raipur' : [21.23,81.63],
    'bilaspur' : [22.09,82.15],
    'janjgir' : [22.02,82.57],
    'kolkata' : [22.57,88.37],
    'mamit' : [23.93,92.48]
    
    }


def locentric(longitude, latitude, database):

	#print longitude,latitude
	client = MongoClient()
	db = client.locationcentric
	collection = db[str(database).strip()]
	#print [database]
	#print [collection.find()]
	#print collection
	#print database
	#print float(longitude)
	latitude = str(latitude)
	longitude = str(longitude)
	results = collection.find({'loc':{'$near':{'$geometry':{'type':"Point",'coordinates':[float(longitude.replace(";","")),float(latitude.replace(";",""))]}}}}).limit(20)
	#print list(results)
	#ans = results

	#print list(results)
	return list(results)


def main(query):
	rm=['near','nearest','nearer','around','close']
	for r in rm :
		query= query.replace(r,"")
#	print query
	key=query.split()

	for i in range(0,len(key)):
		#print loc
		for k,v in loc.items():
			#print key[i],k
			if key[i] in k:
				#print "i am here"
				lat =  v[0]
				lon = v[1]
				query = query.replace(key[i],"")
	
	#print "hoo"
	import Cookie,os
	cookie = Cookie.SimpleCookie()
	stringCookie = os.environ.get('HTTP_COOKIE')
	cor =cookie.load(stringCookie)
	#print stringCookie
#	print stringCookie
	latlong = stringCookie.split(";")
#	print latlong
	lat2 = latlong[0].split("=",1)[1].strip()
	lon2 = latlong[1].split("=",1)[1].strip()
#	print latitude,longitude
	d = math.sqrt(math.pow(lat-lat2,2)+math.pow(lon-lon2,2))
#	print d

	if d > 1:
		longitude=lon
		latitude=lat
	if d < 1:
		longitude=lon2
		latitude=lat2
	ans = locentric(longitude, latitude, query)
#	print latitude,ans
	print ans
	return ans
