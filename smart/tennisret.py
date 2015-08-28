def ret(name,key):
	if "singles" in key and "rank" in key and "current" in key:
		key.remove("rank")
		key.remove("singles")
		key.remove("current")
		key.append("current rank - singles")
	elif "doubles" in key and "rank" in key and "current" in key:
		key.remove("rank")
		key.remove("doubles")
		key.remove("current")
		key.append("current rank - doubles")
	elif "doubles" in key and "rank" in key and "highest" in key:
		key.remove("rank")
		key.remove("doubles")
		key.remove("highest")
		key.append("highest rank - doubles")
	elif "singles" in key and "rank" in key and "highest" in key:
		key.remove("rank")
		key.remove("singles")
		key.remove("highest")
		key.append("highest rank - singles")
	elif "doubles" in key and "rank" in key:
		key.remove("rank")
		key.remove("doubles")
		key.append("current rank - doubles")
		key.append("highest rank - doubles")
	elif "singles" in key and "rank" in key:
		key.remove("rank")
		key.remove("singles")
		key.append("current rank - singles")
		key.append("highest rank - singles")
	elif "rank" in key:
		key.remove("rank")
		key.append("current rank - singles")
		key.append("current rank - doubles")
		key.append("highest rank - singles")
		key.append("highest rank - doubles")
	import pymongo
	d={}
	client=pymongo.MongoClient()
	db=client.kbmain
	tennis1=client.tennis1
	res=list(db.tennis1.find({"name":{"$regex":str(name),"$options":"i"}}).limit(1))
	try:
		res[0].pop("_id")
		li=[]
		for i in key:
			if res[0].has_key(str(i)):
				li.append(i)
		d["required-ans"]=li
		d["main-ans"]=res[0]
		dic=[{"tennis":[d]}]
		return dic
	except:
		return [{}]
def retrank(rank,query):
	if "singles" in query or "individual" in query:
		key="current rank - singles"
	elif "doubles" in query or "dual" in query:
		key="current rank - doubles"
	else:
		key="current rank - singles"
	if "woman" in query or "women" in query or "female" in query:
		key1="woman"
	elif "man" in query or "men" in query or "male" in query:
		key1="man"
	else:
		key1="na"
	import pymongo
	client=pymongo.MongoClient()
	db=client.kbmain
	tennis1=client.tennis1
	try:
		if key1=="na":
			res=list(db.tennis1.find({key:rank}))
		else:
			res=list(db.tennis1.find({key:rank,"sex":str(key1)}))
		if len(res)==0:
			return [{}]
		for r in res:
			r.pop("_id")
		dic=[{"tennis":[{"main-ans":res[0]}]}]
		return dic
	except:
		return [{}]
	

