#MATCH (n:Haryana)-[r]->(m) where type(r)=~ '.*minister.*' return m

from py2neo import Graph,authenticate,Node,Relationship
authenticate("192.168.101.5:7474","neo4j","#srmseONneo4j1")
graph=Graph("http://192.168.101.5:7474/db/data")

def reg_search(query):
	query=query.replace(" of "," ")
	ans=[]
	ans1=[]
	temp=[]
	properties=""
	rquery=query
	catelist=["minister","highway","river"]
	for cc in catelist:
		if cc in rquery:
			#neo_query1="match (n) where n.name=~ '(?i).*%s.*' return n"%(cc)
			#catenode=graph.cypher.execute(neo_query1)
			#print catenode
			rquery=rquery.replace(cc,"")
			clwrd=cc
	query=query.split()
	rquery=rquery.split()
	print rquery
	#neo_query="match (n) where n.name=~ '(?i)%s' return n"%(query)	
	#res=graph.cypher.execute(neo_query)
	for i in range(0,len(rquery)):
		ans=[]
		neo_query1="match (n) where n.name=~ '(?i).*%s.*' return n"%(rquery[i])
		#neo_query2="MATCH (n)-[r]->(m) where type(r)=~ '.*%s.*' return m"%(query[i])
		#res=graph.cypher.execute(neo_query1)
		#ans.append(res)
		res=graph.cypher.execute(neo_query1)
		#print res
		try:
			for kp in res:
				#print kp[0]
				#if kp[0]["name"]==rquery[i]:
				ans.append(kp[0])
			if i==0:
				temp=set(ans)
			else:
				ans=set(ans)
				temp=temp&ans
			#print temp
		except:
			pass
		#print res	
	#ans=list(set(ans))
	ans=list(temp)
	#print ans
	'''for k in query:
		#print ans[k]["name"]
		for j in ans:
			if k in j["name"].lower():
				if k not in temp:
					temp.append(j)
			else:
				continue
	#print temp
	ans=temp'''
	#print ans
	#ans.append(caten)
	print query
	for i in ans:
		for j in query:
			if str(j) != str(i["name"]).lower():
				#print i,j
				n_query="MATCH (n)-[r]->(m) where type(r)=~ '(?i).*%s.*' and n.name=~ '.*%s.*' return m"%(str(j),str(i["name"]))
				res=graph.cypher.execute(n_query)
				try:
					if res[0][0] not in ans:
						r_query="MATCH (n)-[r]->(m) where type(r)=~ '(?i).*%s.*' and n.name=~ '.*%s.*' return r"%(str(j),str(i["name"]))
						ans.append(res[0][0])
						r_res=graph.cypher.execute(r_query)
						#print r_res[0][0].properties
						properties=str(r_res[0][0].properties).encode("utf-8")
				except:
					pass	
	#ans=list(set(ans))
	print ans,properties
	#print len(ans)
				
query=raw_input("Query? ")
orig_query=query
result={}
#print query
query=query.replace(" of "," ").replace("highway","").replace("river","").replace("university","").strip()
neo_query="match (n) where n.name=~ '(?i)%s' return n"%(query)	
res=graph.cypher.execute(neo_query)
if len(res)!=0:	
	#print res
	nnode=res[0][0]
	result["properties"]=nnode.properties
	rquery="match (n)-[r]->(m) where n.name=~ '(?i)"+nnode["name"]+"' return r"
	res1=graph.cypher.execute(rquery)
	for j in res1:
		rtype=j[0].type
		if (result.has_key(rtype)==False):
			nquery="match (n)-[r]->(m) where n.name=~ '(?i)"+nnode["name"]+"' and type(r)=~ '(?i)"+rtype+"' return m,r"
			res2=graph.cypher.execute(nquery)
			#nquery1="match (n)-[r]->(m) where n.name=~ '(?i)"+nnode["name"]+"' and type(r)=~ '(?i)"+rtype+"' return r"
			#res3=graph.cypher.execute(nquery1)
			if len(res2)>1:
				ilist=[]
				for k in res2:
					idata=str((k[0]["name"]))
					iprop=filter(lambda x:ord(x)>31 and ord(x)<128,str((k[1].properties)))
					ilist.append(str(idata+"---"+iprop))
				
					
				result[rtype]=str(ilist)
			else:
				result[rtype]=str(str(res2[0][0]["name"])+"---"+str(res2[0][1].properties)) 
			#res2=list(set(res2))

	#print res2
			#for k in res3:
			#		iprop=str((k[0].properties)).encode("utf-8")
			#		print iprop
	print result
		
else:
	reg_search(orig_query)
