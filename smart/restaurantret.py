#retreival code for the zomato-restaurants module 

'''list of queries handled
	#(restaurant name) restaurant in (city-name)
	#phone no/contact no of (restaurant name) restaurant (location+searching)
	#restaurants near me
	#food places near me
	#places to eat near me
	#where is food-place restaurant in place-name'''

#using mongo database zomato and collection res

import pymongo
client = pymongo.MongoClient()
#using mongo database zomato and collection res
mdb = client['kbmain']
qb=mdb['restaurant']

#fuction for extracting location from server
def locfrmuser():
	import Cookie,os
	cookie = Cookie.SimpleCookie()
	stringCookie = os.environ.get('HTTP_COOKIE')

	cor =cookie.load(stringCookie)
#	print stringCookie
	latlong = stringCookie.split(";")
#	print latlong
	latitude = latlong[0].split("=",1)[1].strip()
	longitude = latlong[1].split("=",1)[1].strip()
	#print latitude,longitude
	lati=float(latitude)
	longi=float(longitude)
	return [longi,lati]

#points=[80.0368023,12.8286149]

#taking input from user
#query=raw_input("Enter? ").lower()
#orig_query=query

#removal of stop words
def resmain(query):
	orig_query=query
	points=locfrmuser()
	#print locfrmuser()
	ans={}
	anslist=[]
	if "restaurant" in query or "restaurants" in query or "place" in query or 'food' in query or 'eat' in query:
		wrd=['restaurants','restaurant','location','address','phone','contact','no.',' no ','contact','near','places','place','me','food','eat',' to ',' is ','where','of ']
		for i in wrd:
			query=query.replace(i,"")
		

		if " in " in query:
			query=query.replace(" in "," ")
			query=query.rsplit(" ",1)
		else:
			query=query.rsplit(" ",1)
			
		
		flag=0 
		
		#checking if query is goes empty after discarding process
		if len(query)!=1:
			resname=query[0].strip()
			place=query[1].strip()
			query1=''
			
			if len(resname)!=0:
				query1="\s?"+str(resname)+"\s?"
			#query2="\s?"+str(place)+"\s?"
				
				#restaurant name and address can be extracted
				if len(place)!=0 and len(query1)!=0:
				
					#check if phone or contact no is asked by user
					if ("contact" in orig_query or "phone" in orig_query) and flag==0:
						for i in qb.find({"title":{"$regex":str(query1),"$options":"i"},"address":{"$regex":str(place),"$options":"i"}}).limit(1):
							i.pop("_id")
							anslist.append(i)
						flag=1

					#searching by restaurant name and place
					results=qb.find({"title":{"$regex":str(query1),"$options":"i"},"address":{"$regex":str(place),"$options":"i"}}).count()
					if(results !=0) and flag==0:
						for i in qb.find({"title":{"$regex":str(query1),"$options":"i"},"address":{"$regex":str(place),"$options":"i"}}):
							i.pop("_id")
							anslist.append(i)
						
						flag=1
					
				#searching only if restaurant name is found
				if ("contact" in orig_query or "phone" in orig_query) and flag==0:
						for i in qb.find({"title":{"$regex":str(query1),"$options":"i"},"loc":{"$near":{"$geometry":{"type":"Point","coordinates":points}}}}).limit(1):
							i.pop("_id")
							anslist.append(i)
						flag=1
				
				#searching for nearest restaurant with the name present
				if query1!='' and flag==0:
						for i in qb.find({"title":{"$regex":str(query1),"$options":"i"},"loc":{"$near":{"$geometry":{"type":"Point","coordinates":points}}}}).limit(10):
							i.pop("_id")
							anslist.append(i)
						flag=1

			#searching for all restaurants near the user's location
			if flag==0:
				for i in qb.find({"loc":{"$near":{"$geometry":{"type":"Point","coordinates":points}}}}).limit(20):
					i.pop("_id")
					anslist.append(i)
				flag=1
			
			#return empty if result is not found
			if flag==0:
				return []
				
			#return result
			if flag==1:
				ans=anslist
				return ans		
