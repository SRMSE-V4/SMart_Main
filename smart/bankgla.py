import aiml
import re
import bankcorpus

def gaiml(query):

	k = aiml.Kernel()
	k.learn("bank_gla.aiml")
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
	disc =bankcorpus.disc
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
def multi_key(orig_query):
	regex="(area served)|(central bank)|(formerly called)|(image source)|(key people)|(native name)|(net income)|(number of employees)|(number of locations)|(operating income)|(rbs group)|(total assets)|(total equity)|(traded as)|(trading name)"
	pattern=re.compile(regex)
	multi_keys=re.findall(pattern,orig_query)
	multi_keys="".join(multi_keys[0])
	return multi_keys
def wordmatrix(query,orig_query):
	fields=[]
	query1=[]
	query2=[]
	try:
		multi_keys=multi_key(orig_query)
		fields.append(multi_keys)
	except:
		pass
	keys=bankcorpus.keys
	keys3=bankcorpus.keys3
	query=query.split(" ")
	for i in range(0,len(query)):
		if query[i] in keys:
			fields.append(query[i])
		elif query[i] in keys3:
			pass
		else:
			query1.append(query[i])
	yield query1
	yield fields
