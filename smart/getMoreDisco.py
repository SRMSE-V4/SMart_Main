#!/usr/bin/python
# Import modules for CGI handling 
import cgi,json,cgitb,json
# Create instance of FieldStorage 
form = cgi.FieldStorage()
cgitb.enable() 
# Get data from fields
num = form.getvalue('num')
query  = form.getvalue('query')
print "Content-type:text/html\r\n\r\n"
import discoret
all_results=discoret.main(query,int(num))
try:
	all_results=all_results[0]["discography"]
except KeyError as e:
	all_results=[]#when no more results
disc={"discography":all_results}
print json.dumps(disc)
		
