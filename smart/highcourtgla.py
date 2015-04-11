import aiml
import re
import highcourtcorpus
dic={"act_established":["act","established","establish"],"benches":["bench","benches"],"chief_justice":["chief","justice"],"judges":["judge"],"seat":["seats","seat"],"founded":["founded","formed","formation"],"name":["name"],"jurisdiction":["jurisdiction"]}
def gaiml(query):

	k = aiml.Kernel()
	k.learn("high_gla.aiml")
	k.setBotPredicate("name", "shiva") 
	query = query.lower()
	query = query.replace(".","")
	query = k.respond(query)
	query = query.lower()
	if "." in query:
		query = query.split(".")
	else:
		query = [query]
	return query

def gdisc(query):
	disc =highcourtcorpus.disc
	query = query.replace("'s","")
	query = query.replace("&","and")
	query = re.sub(r'[^\w]',' ',query)
	key = query.split()
	key2 = query.split()
	for i in range(0,len(key)):
		if key[i] in disc:
			key2.remove(key[i])
	query = " ".join(key2)
	query = query.strip()
	return query

def wordmatrix(query):
	keys1=highcourtcorpus.keys1
	query1=query.split(" ")
	#query2=query.split(" ")
	query2=[]
	fields=[]
	for i in range(0,len(query1)):
		for a in dic:
			if query1[i] in dic[a]:
				fields.append(a)
				break
	for i in range(0,len(query1)):
		if query1[i]  not in keys1:
			query2.append(query1[i])
	yield query2
	yield list(set(fields))
