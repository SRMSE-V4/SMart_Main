import MySQLdb,connection
db= connection.connect("rig")

cursor = db.cursor(MySQLdb.cursors.DictCursor)

def main(query):
        query=query.split()
        
	disc =["conduct","conducted","conducting","commenced","recently","score","needed","held","exam","exams","examinations","course",
               "applicable","courses","degree","pattern","next","date"]
	for i in disc:
		if i in query:
			query.remove(i)
	sql = "SELECT * FROM `exams` WHERE (`name` like '"	
	for i in range(0,len(query)):
		if(i<len(query)-1):
	        	sql = sql+"%"+query[i]
		else:
			sql = sql+"%"+query[i]+"%') LIMIT 1;"
	
#        print sql
	cursor.execute(sql)
	results = cursor.fetchone()
	ans = results
        #print ans
	return ans
