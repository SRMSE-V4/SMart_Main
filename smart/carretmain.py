import carret
import cargla
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer(r'\w+')

def main(query):
	query=query.lower()
	query=str(query)
	query=query.replace("'s","")
	query=query.replace("&","and")
	stop =stopwords.words("english")
	temp=[]
	for i in query.split():
		if i not in stop:
			if tokenizer.tokenize(i):
				temp.append(i)
				#print i
	query=" ".join(temp)
	#print "after nltk :: "
	#print query
	query,key =cargla.wordmatrix(query)
	#print "After wordmarix ::"
	#print query 
	#print key 
	answer=carret.ret(query,key)
	return answer

