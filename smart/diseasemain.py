import diseasegla
import diseaseret
def main(query):
	query=query.replace("diseases","").replace("disease","")
	orig_query=str(query)
	query = diseasegla.gaiml(query)
	for i in query:
		query = diseasegla.gdisc(i)
	query=query.strip()
	query,key=diseasegla.wordmatrix(query)
	query=query.strip()
	answer=diseaseret.ret(query,key)
	return answer
