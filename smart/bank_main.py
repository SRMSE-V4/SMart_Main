import bankgla
import banks_retrieval
def main(query):
	query=query.lower()
	orig_query=str(query)
	query = bankgla.gaiml(query)
	flag = 1
	for i in query:
		query = bankgla.gdisc(i)
	query,fields = bankgla.wordmatrix(query,orig_query)
	if(len(query)>1):
		a=banks_retrieval.ret(query,fields)
                #print a
		if a:
			ans=[{"bank":a}]
		else:
			ans=[{}]
	else:
		ans=[{}]
	return ans

	
