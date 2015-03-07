import json,MySQLdb,re
def difference(text):
	db=MySQLdb.connect("localhost","root","#srmseONserver","rig")
	try:
		query=str(text)
		regex="difference between (.+) and (.+)"
		pattern=re.compile(regex)
		words=re.findall(pattern,query)
		cursor=db.cursor(MySQLdb.cursors.DictCursor)
		sql = """SELECT `Title1` AS title1,`Title2` AS title2,`Titlelink` AS link,`Description` AS description FROM difference WHERE (Title1='%s' and Title2='%s') OR (Title2='%s' and Title1='%s' )"""%(words[0][0],words[0][1],words[0][0],words[0][1])
		#print sql
		cursor.execute(sql)
		qresult=cursor.fetchone()
		qresult["description"]=filter(lambda x:ord(x)>31 and ord(x)<128,qresult["description"]).replace("[","").replace("]","")
		db.close()
		if qresult is None:
			return {}
		return qresult
	except Exception as e:
		db.close()
		return {}
