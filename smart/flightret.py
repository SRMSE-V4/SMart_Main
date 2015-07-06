import pymongo
client=pymongo.MongoClient()
db=client.kbmain
flight=db.flight
def flightbyno(no):
	ans="init"
	res=list(flight.find({"$text":{"$search":str(no)}}))
	if len(res)!=0:
		for row in res:
			if(len(row["flight_details"])==1):
				row.pop("_id")
				ans=row
				answer={"flight":[ans]}
				break
		if ans=="init":
			for i in range(0,len(res[0]["flight_details"])):
				if (str(res[0]["flight_details"][i]["flight_no"]).lower()==str(no)):
					ans=res[0]["flight_details"][i]
					var1=ans["inter_source"]
					var2=ans["inter_destination"]
					ans.pop("inter_source")
					ans.pop("inter_destination")
					ans.update({"source":var1})
					ans.update({"destination":var2})
					answer={"flight":[ans]}
					break
	else:
		answer={}
	return answer
def flightbysoudest(source,dest):
	ansli=[]
	res=flight.find({"source":{"$regex":str(source),"$options":"i"},"destination":{"$regex":str(dest),"$options":"i"}})
	for row in res:
		row.pop("_id")
		ansli.append(row)
	answer={"flight":ansli}
	return answer
