#highway from a to b --
#highway between a and b --
#length of highway nha -- 
#highway nha length --
#highway nha route -- 
#route of highway nha -- 
#highway nha -- 
#length of highway nha in state --
#highway nha length in state -- 
#highway length nha through state --
#length of highway nha through state --
#highway which includes city --
#highway which passes over city --
#highway which passes through city --
#highway which touches city --

from pymongo import MongoClient
import re
client = MongoClient()
db=client['kb']
collection=db['highways']

def find_city_include(city):
	hname=list()
	flag1=0
	des = {}
	data=list(collection.find({"route":{"$exists":1}}))
	#print data
	for i in range(0,len(data)):
		string=data[i]["route"]
		if(str(city) in string):
			flag1=1
			hname.append(data[i]["highway"])
			des = data[i]
	if(flag1==0):
		#print "No highway present in the city"
		d="<NA>"
	else:
		#d=[{"highway":{"highway":hname,"city":str(city)}}]
		d= [{"highway":des}]
	return d
	
def state_length(name,state):
	data=collection.find_one({"highway":str(name)})
	data1=str(data["length_state"])
	r=data1.find(state)
	#print data
	if(r!=-1):
		data1=data1[int(r):]
		data1=data1.split(" (",1)
		data1=data1[1]
		data1=data1.split(")",1)
		data1=str(data1[0])
		#d=[{"highway":{"highway":str(name),"state":str(state),"length_state":str(data1)}}]
		d=[{"highway":data}]
	else:
		#print "Highway not present in the state"
		d="<NA>"
	return d	
	
def routefind(name):
	data=collection.find_one({"highway":str(name)})
	if(str(data)=="None"):
		d="<NA>"
	else:
		#d=[{"highway":{"highway":str(name),"route":data["route"]}}]
		d=[{"highway":data}]
	return d
	
def highwayfind(source,dest):
	flag=0
	hname=list()
	des = {}
	data=list(collection.find({"route":{"$exists":1}}))
	#print data
	for i in range(0,len(data)):
		string=data[i]["route"]
		if(source in string and dest in string):
			flag=1
			hname.append(data[i]["highway"])
			des = data[i]
	if(flag==0):
		#print "No Direct Highway Exists"
		d="<NA>"
	else:
		#d=[{"highway":{"highway":hname,"source":str(source),"destination":str(dest)}}]
		d=[{"highway":des}]
	return d
	
def calc_length(name):
	data=collection.find_one({"highway":str(name)})
	if(str(data)=="None"):
		d="<NA>"
	else:
		#d=[{"highway":{"length_total":data["length_total"],"highway":name}}]
		d=[{"hightway":data}]
	return d
	
def show_details(name):
	data=collection.find_one({"highway":name})
	if(str(data)=="None"):
		d="<NA>"
	else:
		d=[{"highway":data}]
	return d

def get(query):
	if("highway" in query):
		arr=["highway","highways","from","between","through","to","and"]
		for a in range(0,len(arr)):
			if(arr[a] in query):
				query=query.replace(arr[a],"")
		if("nh" in query):
			if("route" in query):
				var=re.search(r'nh\w+',query)
				query=str(var.group())
				ans=routefind(query)
			elif("length" in query):
				query=query.replace("length","")
				v=re.search(r'nh\w+',query)
				name=str(v.group())
				var1=re.search(r'(\w+\s*)+\w*',query)
				query=str(var1.group(1))
				var=re.search(r'nh\w+',query)
				if var:
					query=str(var.group())
					ans=calc_length(query)
				else:
					state=str(query)
					ans=state_length(name,state)
			else:
				var=re.search(r'nh\w+',query)
				query=str(var.group())
				ans=show_details(query)
		else:
			vd=re.search(r'\s\w*\s\s\w*',query)
			if vd:
				query=query.split()
				query=" ".join(query)
				query=query.split(" ",1)
				source=str(query[0])
				dest=str(query[1])
				ans=highwayfind(source,dest)
			else:
				query=query.rsplit(" ",1)
				query=str(query[1])
				ans=find_city_include(query)
	else:
		ans="<NA>"
	#print ans
	return ans
