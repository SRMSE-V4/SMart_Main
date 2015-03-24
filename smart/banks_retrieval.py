def ret(bank,key):
	bank=".*".join(bank)
	bank=".*"+str(bank)+".*"
	samplekey=list()
	from pymongo import MongoClient
	import re
	client = MongoClient()
	db=client.kbmain
	banks_module=db.banks_module
	res=[]
	ans={}
	try:
		for i in range(0,len(key)):
			res.append(list(banks_module.find({"name":{"$regex":str(bank),"$options":"i"},str(key[i]):{"$exists":"true"}})))
			if(res[i]!=[]):
				samplekey.append(key[i]) 
		data=list(banks_module.find({"name":{"$regex":str(bank),"$options":"i"}}))
		data=data[0]
		data.pop('_id')
		ans["required"]=samplekey
		ans["main-ans"]=data
	except:
		ans=[{}]
	return ans
