# flight number 6e276
# flight from delhi to chennai
import flightgla
import flightret
import re
def main(query):
	query=str(query).lower().replace("flights","").replace("flight","").strip()
	v=re.search(r'\w+\d+',query)
	if v:
		no=str(v.group())
		ans=flightret.flightbyno(no)
		return [ans]
	else:
		query = flightgla.gaiml(query)
		for i in query:
			query = flightgla.gdisc(i)
		query=query.split(" ")
		ans=flightret.flightbysoudest(str(query[0]),str(query[1]))
		return [ans]
