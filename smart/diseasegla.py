import aiml
import re
import diseasecorpus
def gaiml(query):
	k = aiml.Kernel()
	k.learn("diseasegla.aiml")
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
	disc =diseasecorpus.disc
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
	key=[]
	flag=0
	query1=query.split(" ")
	query=query.split(" ")
	word=diseasecorpus.word
	for i in word:
		for k in range(0,len(query)):
			if query[k] in word[i]:
				key.append(i)
				query1.remove(query[k])
	key=list(set(key))
	query1=" ".join(query1)
	return query1,key
