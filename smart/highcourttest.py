import highcourtgla
import highcourtret
def main(query):
	query=query.lower()
	if "high" in query:
		query=query.replace("high","")
	if "court" in query:
		query=query.replace("court","")
	if "highcourt" in query:
		query=query.replace("highcourt","")
	query = highcourtgla.gaiml(query)
	#print "#------------------------AIML------------------#"
	#print query
	for i in query:
		query = highcourtgla.gdisc(i)
		#print "#------------------------DISC------------------#"
	query=query.strip()
	query,fields=highcourtgla.wordmatrix(query)
	answer=highcourtret.highcourtret(query,fields)
	return answer

