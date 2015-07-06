import aiml
import re
import flightcorpus
def gaiml(query):

	k = aiml.Kernel()
	k.learn("flightgla.aiml")
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
	disc =flightcorpus.disc
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
