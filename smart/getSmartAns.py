#!/usr/bin/python
import cgi,cgitb,json
form = cgi.FieldStorage() 
print "Content-type:text/html\r\n\r"
f = form.getvalue("q","##123##") #Gets input from the form
import test2
if f!="##123##":
    try:
       result = test2.get(f) #Gets result out of the smart answer module
       #print result
      
       if len(result)!=0:
          result=result[0]
	  #print result
          key=result.keys()[0]
          #print key
          if type(result[key]) is list:
             lisItems =result[key]
	     #print lisItems
             for item in lisItems:
                 if item.has_key('_id'):
                    item.pop('_id')
                 indx=lisItems.index(item)
                 lisItems[indx]=item
             result[key]=lisItems
             print json.dumps(result)
          else:
             if result[key].has_key('_id'):
 	        result[key].pop('_id')
             print json.dumps(result)
       else:
          print "{}"
    except Exception as x:
#       print x
       print "{}"
