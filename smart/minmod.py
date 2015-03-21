from pymongo import MongoClient
import re
import datemin
client = MongoClient()
db=client['kbmain']
collection=db['minister']
def findminister(key,datelist):
	def minfind(key,datelist):
		key=str(key).lower()
		if(len(datelist)==1):
			if(datelist[0]==99999999):
				data=collection.find({"term_end":int(99999999),"ministry":re.compile(str(key),re.IGNORECASE)})
				return data[0]
			else:
				data=collection.find({"term_end":{"$ne":0},"ministry":re.compile(str(key),re.IGNORECASE)})
				for row in data:
					if(int(datelist[0])>=int(row["term_start"]) and int(datelist[0])<=int(row["term_end"])):
						return row
		elif(len(datelist)==2):
			data=collection.find({"term_end":{"$ne":0},"ministry":re.compile(str(key),re.IGNORECASE)})
			for row in data:
				if(int(datelist[0])>=int(row["term_start"]) and int(datelist[0])<=int(row["term_end"]))and (int(datelist[1])>=int(row["term_start"]) and int(datelist[1])<=int(row["term_end"])) :
					return row
		else:
			return "<NA>"
	data=minfind(key,datelist)
	if(str(data)=="None"):
		data="<NA>"
	else:
		data.pop("_id")
		data["term_start"]=datemin.convertdate(data["term_start"])
		data["term_end"]=datemin.convertdate(data["term_end"])
	return [{"ministers":data}]

