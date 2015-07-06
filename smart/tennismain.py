import tennisgla
import tennisret
import re
def main(query):
	query=str(query).lower()
	a=re.search(r'\d+',query)
	if a:
		a=str(a.group())
		ans=tennisret.retrank(str(a),str(query))
	else:
		query=query.replace("tennis","").replace("player","")
		orig_query=str(query)
		query = tennisgla.gaiml(query)
		for i in query:
			query = tennisgla.gdisc(i)
		query=query.strip()
		query,key=tennisgla.wordmatrix(query)
		ans=tennisret.ret(str(query),key)
	return ans
