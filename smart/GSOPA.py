import MySQLdb
#import gla
import connection
db = connection.connect("rig")
cursor = db.cursor(MySQLdb.cursors.DictCursor)

#what is the price of gold today/current
#what is the price of gold 
#gold ?gold_quer
#what is the price in INR/USD of gold today
#what is the price of gold today in gm/g/gram/grams/oz/ounce

def main(query):
    flag=0
    #print query
    result = ""
    gld = ["Gold","Au","Gld","Sona","gold","sona"]
    slv = ["Silver","silver","Ag","Sil","sil","Chandi","chandi"]
    oil = ["crude oil","Crude oil","Crude Oil","oil","Oil","Crude Oil"]
    pet = ["Petrol","Gasoline","petrol","gasoline","petrolium","Petrolium","petroleum","Petroleum"]
    cop = ["copper","Copper","COPPER"]
    alm = ["aluminium","Aluminium","ALUMINIUM"]
    led = ["lead","LEAD","Lead"]
    znc = ["Zinc","zinc","ZINC"]
    nic = ["nickel","Nickel","NICKEL"]
    gas = ["Natural Gas","natural gas","natural Gas","Natural gas"]
    men = ["Mentha Oil","mentha oil","Mentha oil"]
    #print query    
    #query = gla.gdisc(query)
    #print query
    arr=["Delhi","Chennai","Agartala","Aizwal","Bengaluru","Bhubhaneswar","Gangtok","Guwahati","Hyderabad","Itanagar","Jalandhar","Kohima"," Kolkata"," Mumbai","Navi Mumbai","Panjim","Pimpri","Port Blair","Raipur","Ranchi","Shimla","Surat","Trivandrum","Ahmedabad","Ambala","Bhopal","Chandigarh","Dehradun","Gandhinagar","Gurgaon","Gwalior","Imphal","Jaipur","Jammu","Kolhapur","Lucknow","Mysore","Noida","Patna","Pondicherry","Pune","Rajkot","Shillong","Srinagar","Thane","Vadodara"] 
    key=query.split()
    for i in range(0,len(key)):
	if key[i] in gld:
	    flag = 1
	    result=today("gold")
	    #print result
	    #query = disc(query)
	    if query!="":
                result=today("gold")
                #print result
		return result
                break
	if key[i] in slv:
	    flag = 1
	    result=today("silver")
	    #print result
	    #query = disc(query)
	    if query!="":
                result=today("silver")
                return result
                break
	if key[i] in oil:
	    flag = 1
	    result=today("crude oil")
	    #print result
	    #query = disc(query)
	    if query!="":
                result=today("crude oil")
                return result
                break
        if key[i] in pet:
            flag = 1
            for j in range(0,len(key)):
		#print j
                if key[j].capitalize() in arr:
                        
            		result3=tod(key[j])
		        return result3
			break
		elif key[j] not in pet:
			result3=tod("Delhi")
			return result3
			break 
            #print result
            #query = disc(query)
            if query!="":
		#print key[j],j
                #result3=tod(key[j])
                return result3
                break
                
	if key[i] in cop:
	    flag = 1
	    result=today("copper")
	    #print result
	    #query = disc(query)
	    if query!="":
                result=today("copper")
                return result
                break   
                             
	if key[i] in alm:
	    flag = 1
	    result=today("aluminium")
	    return result
	    #query = disc(query)
	    #if query!="":
            #    result=today("aluminium")
                #print result
            #    break
                
	if key[i] in led:
	    flag = 1
	    result=today("lead")
	    return result
	    #query = disc(query)
               
	if key[i] in znc:
	    flag = 1
	    result=today("zinc")
	    return result
                
	if key[i] in nic:
	    flag = 1
	    result=today("nickel")
	    return result


def today(nme):
	result = ""
	sql="SELECT `name`,`value`FROM `minerals` WHERE `name` like '%"+nme+"%';"
	cursor.execute(sql)
        result=cursor.fetchall()
	#print result
	return result

def tod(nme):
    result = ""
    sql="SELECT `name`, `place`,`value` FROM `petrol` WHERE `place` like '%"+nme+"%';"
    cursor.execute(sql)
    result=cursor.fetchall()
    #print result
    return result

#, `Percentage_Change`, `High`, `Low`, `Open`, `Close`, `Net_change`



