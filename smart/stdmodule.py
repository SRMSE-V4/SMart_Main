#std code of chennai 
#chennai std code
#stdcode of chennai
#chennai stdcode 
#name the city whose std code is 044
#044 is the std code of which city
def stdcodemod(query):
	def find1(q):
		try:
			res=collection.find({"Location":{"$regex":str(q),"$options":"x","$options":"i"}})
			answer=[{"general":{"Location":str(res[0]["Location"]).strip(),"std_code":str(res[0]["std_code"]).strip()}}]
		except:
			answer=[]
		return answer
	def find2(q):
		try:
			a=list()
			res=collection.find({"std_code":str(q)})
			for row in res: #423 is the std code of ooty and coonoor
				a.append(str(row["Location"]).strip())
			answer=[{"general":{"Location":",".join(a),"std_code":str(q)}}]
		except:
			answer="<NA>"
		return answer
	from pymongo import MongoClient
	import re
	client = MongoClient()
	db=client['kbmain']
	collection=db['std_codes']
	#query=raw_input("Enter Your Query:- ").lower()
	if("stdcode" in query or "std code" in query):
		query=query.replace("stdcode","")
		query=query.replace("of","")
		query=query.replace("std code","")
		query=query.strip()
		var=re.search(r'\d+',query)
		if(len(query)!=0):
			if not var:
				ans=find1(query)
			else:
				stdcode=var.group(0)
				if(int(stdcode[0])==0):
					stdcode=stdcode[1:]
				stdcode=" "+str(stdcode)+" "
				ans=find2(str(stdcode))
		else:
			ans=[]
	else:
		ans=[]
	return ans

