import pymongo
client=pymongo.MongoClient()
db=client.kbmain
disease=db.disease
def ret(query,key):
	abc=list(disease.find({"title":str(query)}))
	if(len(abc)==0):
		res=list(disease.find({"title":{"$regex":str(query),"$options":"i"}}))
		if len(res)==0:
			ans=[{}]
			return ans
		else:
			try:
				a=res[0]
				a.pop("_id")
				ans=[{"disease":{"required-ans":key,"main_ans":[a]}}]
			except:
				ans=[{}]
		return ans
	else:
		try:
			ax=abc[0]
			ax.pop("_id")
			ans=[{"disease":{"required-ans":key,"main_ans":[ax]}}]
		except:
			ans=[{}]
		return ans
			
	
