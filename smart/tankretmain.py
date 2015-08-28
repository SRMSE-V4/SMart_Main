import tankret
import tankgla
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer(r'\w+')
def main(query):
	query=query.lower().replace("tanks","").replace("tank","")
	query=str(query)
	query=query.replace("'s","").replace("&","and")
	stop=stopwords.words("english")
	temp=[]
	for i in query.split():
		if i not in stop:
			if tokenizer.tokenize(i):
				temp.append(i)
	query=" ".join(temp)
	query,key=tankgla.wordmatrix(query)
	key="".join(key)
	answer=tankret.ret(query,key)
	return answer
