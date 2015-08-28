import pymongo
client=pymongo.MongoClient()
db=client.kbmain
cars=db.car
def ret(query, key):
	abc=list((cars.find({"carname":str(query)})))
	#print abc
	if(len(abc)==0):
		res=list(cars.find({"carname":{"$regex":str(query),"$options":"i"}}))	
		if(len(res)==0):
			ans=[{}]
			return ans
		else:
			try:
				a=res[0]
				a.pop("_id")
				ans=[{"car":{"required-ans":key,"main_ans":[a]}}]
				return ans
			except:
				ans=[{}]
	else:
		try:
			ax=abc[0]
			ax.pop("_id")
			ans=[{"car":{"required-ans":list(cars.find({key:{"regex":str(query),"options":"i"}})),"main_ans":[a]}}]
			return ans	
		except:
			ans=[{}]
			return ans
			
				

