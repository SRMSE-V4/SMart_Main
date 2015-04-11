

#*.com www.*.com
from pymongo import MongoClient
client=MongoClient()
db=client.kbmain
top_pages4=db.top_pages4
def ret(query,fields):
	res=[]
	ans={}
	samplekey=[]
	try:
		for i in range(0,len(fields)):
			res.append(list(top_pages4.find({"title":{"$regex":str(query),"$options":"i"},str(fields[i]):{"$exists":"true"}})))
			if (res[i]!=[]):
				samplekey.append(fields[i])
		data=top_pages4.find({"title":{"$regex":str(query),"$options":"i"}}).limit(1)
		data=data[0]
		data.pop('_id')
		ans["required"]=samplekey
		ans["main-ans"]=data
		answer=[{"site":ans}]
	except:
		answer=[{}]
	return answer
