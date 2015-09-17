#MATCH (n:Haryana)-[r]->(m) where type(r)=~ '.*minister.*' return m

from py2neo import Graph,authenticate,Node,Relationship
authenticate("ip","neo4j","password")
graph=Graph()

def reg_search(query):
	l=[]
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
	check="name"
	c=0
	if "chief" in query:
		query.remove("chief")
		rquery=rquery.replace("chief","").strip()
		check="image"
		c=1
	elif "college" in query or "university" in query:
		check="address"
	elif "high court" in query:
		check="chief_justice"
	rquery=rquery.split()
	#print rquery
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
	#print query
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
						properties=r_res[0][0].properties
				except:
					pass	
	#ans=list(set(ans))
	for i in ans:
		if i.properties.has_key(check):
			if c==1:
				if i.properties[check].startswith("upload"):
					d1=i.properties
					d1.update(properties)
					l.append(d1)
			else:	
				d1=i.properties
				d1.update(properties)
				l.append(d1)
#	d1.update(d2)
#	print d1
	#print len(ans)
	print l
				
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
	#print res1
	for j in res1:
		rtype=j[0].type
		#print rtype
		if (result.has_key(rtype)==False):
			nquery="match (n)-[r]->(m) where n.name=~ '(?i)"+nnode["name"]+"' and type(r)= '"+rtype+"' return m,r"
			res2=graph.cypher.execute(nquery)
			#nquery1="match (n)-[r]->(m) where n.name=~ '(?i)"+nnode["name"]+"' and type(r)=~ '(?i)"+rtype+"' return r"
			#res3=graph.cypher.execute(nquery1)
			#print nquery,res2
			if len(res2)>1:
				ilist=[]
				for k in res2:
					idata=str((k[0]["name"]))
					iprop=filter(lambda x:ord(x)>31 and ord(x)<128,str(k[1].properties))
					if len(iprop)!=0:
						u=[]
						u.append(str(idata))
						u.append(k[1].properties)
						ilist.append(u)
					else:
						ilist.append([str(idata)])
				
					
				result[rtype]=ilist
			else:
				temp=res2[0][1].properties
				if len(temp)!=0:
					l=[]
					l.append(str(res2[0][0]["name"]))
					l.append(res2[0][1].properties)
					result[rtype]=l 
				else:
					result[rtype]=[str(res2[0][0]["name"])]			
				#res2=list(set(res2))

	#print res2
			#for k in res3:
			#		iprop=str((k[0].properties)).encode("utf-8")
			#		print iprop
	print result
		
else:
	reg_search(orig_query)
