import pymongo
from pymongo import MongoClient
import json
import re
client = MongoClient('localhost', 27017)
db=client.kbmain
artists_final=db.artists_final
def ret(artist_name,n):
	if (re.match(r'\d|\w',artist_name))==None:
		return	{}		
	else:
		result=[]
		resl1=[]
		if n==0:
			resl=artists_final.find({"artist":{"$regex":str(artist_name),"$options":"i"},}).sort("release_date",-1)
		else:
			resl=artists_final.find({"artist":{"$regex":str(artist_name),"$options":"i"},}).sort("release_date",-1).skip(n)
		for item in resl:
			item.pop("_id")
			resl1.append(item)
		#print len(resl1)
		if len(resl1)!=0:
			result=resl1
			result={"discography":result}
			#print result
			return [result]
		else:
			result={}
			return [result]
def main(query,n):
	query=query.lower()
	query=query.replace("discography of ","").replace("albums of ","").replace("discography","").replace("albums","")
	query=re.sub("\s+"," ",query).strip()

	res=ret(query,n)
	return res


