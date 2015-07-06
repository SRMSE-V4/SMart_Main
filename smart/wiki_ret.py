from pymongo import MongoClient
client=MongoClient()
db=client["wiki_dumps"]
collection1=["collection1"]
def findwiki(query,no):
	row=db.collection1.find({"infobox.name.text":{"$regex":"^"+str(query)+"$","$options":"is"}}).sort("infobox.name.text",1).limit(no)
	a=list(row)
	if(len(a)==0):
		row=db.collection1.find({"infobox.Name.text":{"$regex":"^"+str(query)+"$","$options":"is"}}).sort("infobox.Name.text",1).limit(no)
		a=list(row)
	if a:
		a[0].pop('_id')
		return [{"wiki":a[0]}]
	else:
		return [{}]
#query=raw_input("Enter:- ").lower()
#query1=query
#no=len(query1.split(" "))
#findwiki(query,no)
