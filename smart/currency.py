from itertools import permutations
import gla
import corpus

def getcomb(inp): #Getting possible combinations of the given input
	comb = []
	for i in range(1,len(inp)+1):
		for x in permutations(inp,i):
			temp = ""
			for k in range(0,i):
				temp = temp+" "+x[k]
			temp = temp.strip()
			comb.append(temp)
	comb.sort(key=len)
	comb = comb[::-1]
	return comb

def get(query):
	ans = "<NA>"
	comb = getcomb(query.split())
	curr = corpus.curr
	wtn,query = gla.getwordtonum(query.split())
	if wtn!='<NA>':
		value = wtn[0][0]
	else:
		value = 1
	asked = []
	temp = []
	index = []
	splitter = query.split()
	for i in comb:
		if i in curr.keys():
			asked.append(curr[i])
			tempsplit = i.split()
			index.append(splitter.index(tempsplit[0]))
	for i in asked:
		temp.append(i.split())
	for i in range(0,len(temp)):
		for j in range(i+1,len(temp)):
			common = list(set(temp[i])&set(temp[j]))
			if len(common)>0:
				if len(asked[i])>len(asked[j]):
					asked.remove(asked[j])
					index.remove(index[j])
				elif len(asked[i])<len(asked[j]):
					asked.remove(asked[i])
					index.remove(index[i])
	subject = ""
	object = ""
	subject = subject+asked[index.index(min(index))]
	asked.remove(subject)
	object = object+asked[0]
	ans = [{"currency":{"given":subject,"value":value,"asked":object}}]
	return ans
