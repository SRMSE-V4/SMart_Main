import pymongo
import ast
client=pymongo.MongoClient()
db=client.kbmain
tanks=db.tank
def remove(resl):
	final=[]
	tmp_final=list(set(resl))
	for i in tmp_final:
		final.append(ast.literal_eval(i))
		#print final
	return final
def ret(query,key):
	
	abc=list(tanks.find({key:str(query)}))
	#print len(abc)
	resl=[]
	if (len(abc)==0):
		
		res=list(tanks.find({key:{"$regex":str(query),"$options":"i"}}))
		#print res
		if(len(list(res))==0):
			ans=[{}]
		
			return ans
		else:
			for item in res:
				item.pop("_id")
			
			
				resl.append(str(item))
			
			result=remove(resl)
			ans=[{"tank":result}]
			return ans
