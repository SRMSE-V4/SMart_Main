import aiml
import re
import toppgcorpus
def wordmatrix(query):
	fields=[]
	keys=toppgcorpus.keys
	query=query.split(" ")
	for i in range(0,len(query)):
		if query[i] in keys:
			fields.append(query[i])
	return fields
