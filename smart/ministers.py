import dateconvert
import minmod
import re
dept=["broadcast","broadcasting","water","agriculture","finance","health","home","law","minority","overseas","panchayatiraj","panchayati raj","parliament","rail","science","shipping","road","transport","highway","tribal","water","defence","aviation","information","external","human resource development","education"]
#query=raw_input("Enter Query:- ").lower()
def main(query):
	query=query.replace("-","/")
	dept1=" "
	datelist=[]
	regex=re.search(r'\d{4}',str(query))
	if "minister" in query:
		for i in range(0,len(dept)):
			if dept[i] in query:
				dept1=dept[i]
				break
	if "present" in query:
		datelist.append(99999999)
	elif regex:
		reg="(\d{1,2}\s(jan[a-z]*|feb[a-z]*|mar[a-z]*|apr[a-z]*|may[a-z]*|jun[a-z]*|jul[a-z]*|aug[a-z]*|sep[a-z]*|oct[a-z]*|nov[a-z]*|dec[a-z]*)\s\d{4})|((jan[a-z]*|feb[a-z]*|mar[a-z]*|apr[a-z]*|may[a-z]*|jun[a-z]*|jul[a-z]*|aug[a-z]*|sep[a-z]*|oct[a-z]*|nov[a-z]*|dec[a-z]*)\s\d{4})|(\d{1,2}\/\d{1,2}\/\d{4})|((\d{1,2}\-\d{1,2}\-\d{4}))|((\d{1,2}\-\w{1,9}\-\d{4}))|(\d{1,2}\/\w{1,9}\/\d{4})|(\d{4})"
		pattern=re.compile(reg)
		dates=re.findall(pattern,query)
		if(len(dates)==2):
			elem=dates[0]
			an=str("".join(elem))
			regex1="(.*\d{4}).*"
			pattern=re.compile(regex1)
			an=re.findall(pattern,an)
			fdate=dateconvert.convert(str(an[0]))
			datelist.append(int(fdate))	
			elem=dates[1]
			an=str("".join(elem))
			regex1="(.*\d{4}).*"
			pattern=re.compile(regex1)
			an=re.findall(pattern,an)
			fdate=dateconvert.convert(str(an[0]))
			datelist.append(int(fdate))
		elif(len(dates)==1):
			elem=dates[0]
			an=str("".join(elem))
			an=str("".join(elem))
			regex1="(.*\d{4}).*"
			pattern=re.compile(regex1)
			an=re.findall(pattern,an)
			fdate=dateconvert.convert(str(an[0]))
			datelist.append(int(fdate))
	elif len(dept1)>3:
		datelist.append(99999999)
	try:
		answer=minmod.findminister(dept1,datelist)
		return answer
	except:
		return []
