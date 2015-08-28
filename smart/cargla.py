import re
import carcorpus

def wordmatrix(query):
	key=[]
	flag=0
	query1=query.split(" ")
	query=query.split(" ")
	keys=carcorpus.keys
	for i in keys:
		for k in range(0,len(query)):
			if query[k] in keys[i]:
				key.append(i)
				#print key
				query1.remove(query[k])
	key=list(set(key))
	query1=" ".join(query1)
	#print key
	#print "*********"
	#print query1
	return query1,key

#wordmatrix("martui suzuki swift fuel type")
