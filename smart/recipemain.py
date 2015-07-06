import recipegla
import reciperet
def main(query):
	try:
		query=query.replace("recipes","").replace("recipe","")
		orig_query=str(query)
		query = recipegla.gaiml(query)
		for i in query:
			query = recipegla.gdisc(i)
		query=query.strip()
		query,key=recipegla.wordmatrix(query)
		query=query.strip()
		answer=reciperet.ret(query,key)
	except:
		answer=[{}]
	return answer
