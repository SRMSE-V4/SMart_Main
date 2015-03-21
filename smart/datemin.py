def convertdate(query):
	query=str(query)
	if query=="99999999":
		return "Present"
	else:
		year=query[0:4]
		month=query[4:6]
		date=query[6:]
		if(int(date)==0):
			date=""
		if(int(month)<1 or int(month)>12):
			month=""
			date=""
		month=month.replace("01"," January ")
		month=month.replace("02"," Febuary ")
		month=month.replace("03"," March ")
		month=month.replace("04"," April ")
		month=month.replace("05"," May ")
		month=month.replace("06"," June ")
		month=month.replace("07"," July ")
		month=month.replace("08"," August ")
		month=month.replace("09"," September ")
		month=month.replace("10"," October ")
		month=month.replace("11"," November ")
		month=month.replace("12"," December ")
		finaldate=(str(date)+str(month)+str(year)).strip()
		return finaldate
convertdate(20160531)
