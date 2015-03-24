#theatre-name showtimes/shows in place-name(2)(done)
#theatres in place-name(1)(done)
#theatres place-name(done)
#theatres in place-name showing movie-name(2)(done)
#movie-name timings/times/shows/showtimes in place-name(2)(done)
#movie-name timings/times/shows/showtimes in theatre-name place-name(3)(done)
#theatres which/that show movie-name in place-name(2)(done)
#theatres showing movie-name in place-name(2)(done)
#theatre-name timings in place-name(2)(done)
#movie-name place-name(done)
#theatre-name place-name(done)
#shows in theatre-name place-name(done)
#movie-name in place-name(done)
#movie schedule in theatre-name(done)
import re
import MySQLdb
def thea_ret(query):
        import MySQLdb,connection
        db= connection.connect("rig")
	cursor=db.cursor(MySQLdb.cursors.DictCursor)
	def display(flag):
		c=[]
		#print "in display"
		result=cursor.fetchall()
		#print result
		if flag==1:
			for row in result:
				th_name=row[1]
				city=row[3]
				m_name=row[5]
				times=row[7]
				#print str(th_name)+" "+str(city)+" "+str(m_name)+" "+str(times)
				d=[{"t_name":th_name,"times":times}]
				c.append(d)
			disp={"theatre":{"place":city,"moviename":m_name,"theatre_and_times":c}}
			#print disp
		if flag==2:
			for row in result:
				th_name=row[1]
				city=row[3]
				m_name=row[5]
				times=row[7]
				d=[{"moviename":m_name,"times":times}]
				c.append(d)
			disp={"theatre":{"place":city,"t_name":th_name,"movie_and_times":c}}
		if flag==3:
			for row in result:
				th_name=row[1]
				city=row[3]
				m_name=row[5]
				times=row[7]
				d=[{"place":city,"times":times}]
				c.append(d)
			disp={"theatre":{"t_name":th_name,"moviename":m_name,"place_and_times":c}}
		return disp
		#d=[{"theatres":{"theatre name":str(th_name),"city name":str(city),"movie name":str(m_name),"times":str(times)}}]

	def display1():
		d_list=[]
		result=cursor.fetchall()
		for row in result:
			d_list.append(row[0])
		d=[{"theatre":{"theatre-list":d_list}}]
		return d

	def find3(var1,var2):
		temp=var2
		try:
			var2=var2.rsplit(" ",1)
			res1=var1
			res2=var2[0]
			res3=var2[1]
			#print str(res1)+" "+str(res2)+" "+str(res3)
			sql="SELECT * from `showtimes` where `city`='%s' and `moviename` LIKE '%s' and `theatrename` LIKE '%s';"%(str(res3),str("%"+res1+"%"),str("%"+res2+"%"))
			res=cursor.execute(sql)
			if not res:
				find2(var1,temp)
			else:
				x=display(4)
			return x
		except:
			#print "calling function"
			return find2(var1,temp)
		
	def find2(res1,res2):
		done=0
		#print res1
		#print res2
		#x=find3(res1,res2)
		sql="SELECT * from `showtimes` where `city`='%s' and `moviename` LIKE '%s';"%(str(res1),str("%"+res2+"%"))
		res=cursor.execute(sql)
		#print sql
		dat= cursor.fetchall()
		if not dat:
			sql1="SELECT * from `showtimes` where `city`='%s' and `moviename` LIKE '%s';"%(str(res2),str("%"+res1+"%"))
			#print sql
			re=cursor.execute(sql1)
			#dat = cursor.fetchall()
			#print dat
			if re:
				x=display(1)
				done=done+1
		elif done==0:
			x=display(1)
			done=done+1
				
		sql1="SELECT * from `showtimes` where `theatrename` LIKE '%s' and `city`='%s';"%(str("%"+res1+"%"),str(res2))
		res=cursor.execute(sql1)
		if not res and done==0:
			sql1="SELECT * from `showtimes` where `theatrename` LIKE '%s' and `city`='%s';"%(str("%"+res2+"%"),str(res1))
			res=cursor.execute(sql1)
			if res:
				x=display(2)
				done=done+1
		elif done==0:
			x=display(2)
			done=done+1
	
		sql1="SELECT * from `showtimes` where `theatrename` LIKE '%s' and `moviename`='%s';"%(str("%"+res1+"%"),str(res2))
		res=cursor.execute(sql1)
		if not res and done==0:
			#print "hi"
			sql1="SELECT * from `showtimes` where `theatrename` LIKE '%s' and `moviename`='%s';"%(str("%"+res2+"%"),str(res1))
			res=cursor.execute(sql1)
			if res:
				x=display(3)
				done=done+1
		elif done==0:
			x=display(3)
			done=done+1
		if done==0:
			return "n/a"
		return x

	def find1(inp):
		sql2="SELECT distinct(`theatrename`) from `showtimes` where `city`='%s';"%(str(inp))
		res=cursor.execute(sql2)
		if not res:
			return "n/a"
		else:
			x=display1()
		return x
			
			
	#query=raw_input("Enter your query : ").lower()
	query=query.replace("which ","")
	query=query.replace("that ","")
	query=query.replace("are ","")
	query=query.replace("what ","")
	query=query.replace("where ","")
	query=query.replace("currently ","")
	query=query.replace("includes ","")
	query=query.replace("have","")
	query=query.replace("schedule","")
	query=query.replace("  "," ")
	#print query
	c=0
	seobj=re.search(r'theat\w* in (.*) show\w* (.*)$',query,re.I|re.M)
	if seobj and c==0:
		var1=seobj.group(1)
		var2=seobj.group(2)
		result=find2(var1,var2)
		c=c+1
	seobj=re.search(r'theat\w* show\w* (.*) in (.*)$',query,re.I|re.M)
	if seobj and c==0:
		var1=seobj.group(1)
		var2=seobj.group(2)
		result=find2(var1,var2)
		c=c+1	
	seobj=re.search(r'theat\w* in (\w*\s?\w*)$',query,re.I|re.M)
	if seobj and c==0:
		var=seobj.group(1)
		#print var
		result=find1(var)
		c=c+1
	seobj=re.search(r'(.*) tim\w* in (.*)',query,re.I|re.M)
	if seobj and c==0:
		var1=seobj.group(1)
		var2=seobj.group(2)
		result=find3(var1,var2)
		c=c+1
	seobj=re.search(r'theat\w* (\w*) (\w*) (.*) in (.*)$',query,re.I|re.M)
	if seobj and c==0:
		var1=seobj.group(3)
		var2=seobj.group(4)
		result=find2(var1,var2)
		c=c+1
	seobj=re.match(r'shows in (.*)$',query,re.I|re.M)
	if seobj:
		var=str(seobj.group(1))
		find1(var)
		var=var.rsplit(" ",1)
		var1=str(var[0])
		var2=str(var[1])
		result=find2(var1,var2)
		c=c+1
	seobj=re.search(r'(.*) show\w* in (.*)$',query,re.I|re.M)
	if seobj and c==0:
		var1=seobj.group(1)
		var2=seobj.group(2)
		result=[find3(var1,var2)]
		c=c+1
	seobj=re.search(r'(\w*) theat\w*$',query,re.I|re.M)
	if seobj and c==0:
		var=seobj.group(1)
		result=find1(var)
		c=c+1
	seobj=re.search(r'(.*) in (.*)$',query,re.I|re.M)
	if seobj and c==0:
		var1=seobj.group(1)
		var2=seobj.group(2)
		result=find2(var1,var2)
		c=c+1
	seobj=re.search(r'^theat(\w*) (\w+)$',query,re.I|re.M)
	if seobj and c==0:
		var=seobj.group(2)
		result=find1(var)
		c=c+1
	if c==0:
		query=query.rsplit(" ",1)
		var1=""
		var2=""
		try:
			var1=query[0]
			var2=query[1]
		except:
			var1="chennai"#put default location here
			var2=query[0]
		result=find2(var1,var2)
	#print (result)	
	#print result
	return result                    #will return not found if no results are found
