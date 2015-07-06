import pymongo
client=pymongo.MongoClient()
db=client.kbmain
recipes=db.recipes
def ret(query,key):
	abc=list(recipes.find({"name":str(query)}))
	if(len(abc)==0):
		res=list(recipes.find({"name":{"$regex":str(query),"$options":"i"}}))
		if len(res)==0:
			ans=[{}]
			return ans
		else:
			try:
				a=res[0]
				a.pop("_id")
				ans=[{"recipe":{"required-ans":key,"main_ans":[a]}}]
			except:
				ans=[{}]
		return ans
	else:
		try:
			ax=abc[0]
			ax.pop("_id")
			ans=[{"recipe":{"required-ans":key,"main_ans":[ax]}}]
		except:
			ans=[{}]
		return ans
			
	
