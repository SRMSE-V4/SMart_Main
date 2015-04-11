def highcourtret(query,key):
	query=".*".join(query)
	query=".*"+str(query)+".*"
	samplekey=list()
	from pymongo import MongoClient
	import re
	client = MongoClient()
	db=client.kbmain
	highcourts=db.highcourts
	res=[]
	ans={}
	try:
		for i in range(0,len(key)):
			res.append(list(highcourts.find({"name":{"$regex":str(query),"$options":"i"},str(key[i]):{"$exists":"true"}})))
			if(res[i]!=[]):
				samplekey.append(key[i]) 
		data=list(highcourts.find({"name":{"$regex":str(query),"$options":"i"}}))
		data=data[0]
		data.pop("_id")
		ans["required"]=samplekey
		ans["main-ans"]=data
		mainans=[{"highcourt":ans}]
	except:
		mainans=[{}]
	return mainans
