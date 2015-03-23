from pymongo import MongoClient
client=MongoClient()
db=client["wiki"]
collection1=["collection1"]
def findwiki(query,no):
	row=db.collection1.find({"infobox.name.text":{"$regex":str(query),"$options":"i"}}).limit(no)
	a=list(row)
	if(len(a)==0):
		row=db.collection1.find({"infobox.Name.text":{"$regex":str(query),"$options":"i"}}).limit(no)
		a=list(row)
	print a
query=raw_input("Enter:- ").lower()
query1=query
no=len(query1.split(" "))
findwiki(query,no)
