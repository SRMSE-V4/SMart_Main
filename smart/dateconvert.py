def convert(dat):
	import re
	dat=dat.replace("/"," ").replace("-"," ")
	dateparts=dat.split()
	if len(dateparts)>2:
		if len(dateparts[0])==1:
			dateparts[0]="0"+dateparts[0]
		dateparts[1]=dateparts[1].lower().replace("january","01").replace("jan","01")
		dateparts[1]=dateparts[1].lower().replace("february","02").replace("feb","02")
		dateparts[1]=dateparts[1].lower().replace("march","03").replace("mar","03")
		dateparts[1]=dateparts[1].lower().replace("april","04").replace("apr","04")
		dateparts[1]=dateparts[1].lower().replace("may","05").replace("may","05")
		dateparts[1]=dateparts[1].lower().replace("june","06").replace("jun","06")
		dateparts[1]=dateparts[1].lower().replace("july","07").replace("jul","07")
		dateparts[1]=dateparts[1].lower().replace("august","08").replace("aug","08")
		dateparts[1]=dateparts[1].lower().replace("september","09").replace("sept","09")
		dateparts[1]=dateparts[1].lower().replace("october","10").replace("oct","10")
		dateparts[1]=dateparts[1].lower().replace("november","11").replace("nov","11")
		dateparts[1]=dateparts[1].lower().replace("december","01").replace("dec","12")
		temp=dateparts[0]
		dateparts[0]=dateparts[2]
		dateparts[2]=temp
	elif(len(dateparts)==2):
		dateparts.insert(0,"01")
		dateparts[1]=dateparts[1].lower().replace("january","01").replace("jan","01")
		dateparts[1]=dateparts[1].lower().replace("february","02").replace("feb","02")
		dateparts[1]=dateparts[1].lower().replace("march","03").replace("mar","03")
		dateparts[1]=dateparts[1].lower().replace("april","04").replace("apr","04")
		dateparts[1]=dateparts[1].lower().replace("may","05").replace("may","05")
		dateparts[1]=dateparts[1].lower().replace("june","06").replace("jun","06")
		dateparts[1]=dateparts[1].lower().replace("july","07").replace("jul","07")
		dateparts[1]=dateparts[1].lower().replace("august","08").replace("aug","08")
		dateparts[1]=dateparts[1].lower().replace("september","09").replace("sept","09")
		dateparts[1]=dateparts[1].lower().replace("october","10").replace("oct","10")
		dateparts[1]=dateparts[1].lower().replace("november","11").replace("nov","11")
		dateparts[1]=dateparts[1].lower().replace("december","01").replace("dec","12")
		temp=dateparts[0]
		dateparts[0]=dateparts[2]
		dateparts[2]=temp
	else :
		if dateparts[0].lower()=="incumbent":
			dateparts[0]="99999999"
		elif dateparts[0].lower()=="none":
			dateparts[0]="-1"
		else:
			dateparts.append("00")
			dateparts.append("00")
	dateparts="".join(dateparts)
	return int(dateparts)
