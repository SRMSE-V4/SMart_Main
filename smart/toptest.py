import toppgcorpus
import toppgret
import topgla
def main(query):
	query1=query
	#print query
	if "." in query:
		query=query.split(".")
		if(len(query)==3):
			query=str(query[1])
		elif(len(query)==2):
			query=str(query[0])
		if " " in query:
			query=query.rsplit(" ",1)
			query=str(query[1])
	fields=topgla.wordmatrix(query1)
	answer=toppgret.ret(query,fields)
	return answer
