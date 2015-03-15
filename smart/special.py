
def getanswer(msg,query,orig_query):
	if msg == "<train status>":
		ans = train(query)
	elif msg == "<weather status>":
		ans = weather(query)
        elif msg == "<cricinfo module>":
                ans = cric_info(orig_query)

	elif msg == "<stock status>":
		ans = stock(query)
	elif msg == "<mineral status>":
		ans = mineral(query)
	elif msg == "<sports status>":
		ans = sports(query)
	elif msg == "<movie review>":
		ans = movie(query,orig_query)
        elif msg == "<exam status>":
                ans = exam(query)
        elif msg == "<locationcentric module>":
                ans = location(query)
	elif msg == "<highway module>":
                ans = highway(query)
	elif msg == "<differences module>":
                ans = differences(orig_query)
	elif msg == "<currency module>":
		ans = currency(query) 
	elif msg == "<meanings module>":
		ans= meanings(orig_query)  
        elif msg == "<theatre module>":
                ans= theatre(orig_query)

        elif msg == "<std module>":
                ans= std(query)


	#print "here"             
	return ans



def std(query):
        ans = {}
        import stdmodule as st
        #print query
	ans = st.stdcodemod(query)
        #print ans
        if ans:
                return ans
        else:
                return [{}]





def cric_info(query):
        ans = {}
        import cricinfo as cric
        ans = cric.getQuery(query)
        #print ans
        if ans:
                return ans
        else:
                return [{}]



def theatre(query):
        ans = {}
        import theatreMain as th
        ans = th.theatre(query)
	#print ans
        if ans:
                return ans
        else:
                return [{}]


def meanings(query):
	ans = {}
	import meaning as mn
	ans = mn.main(query)
	if ans["dict"]:
		return [ans]
	else:
		return [{}]
	
def currency(query):
	ans = "<NA>"
	import currency
	ans = currency.get(query)
	return ans

def highway(query):
	ans = "<NA>"
	import highway1
	ans = highway1.highwaymod(query)
	return ans

def differences(query):
	import difference as dif
	
	ans = "<NA>"
	getAns= dif.difference(query)
	if getAns: 
		ans = [{"differences":dif.difference(query)}]
	else:
		ans =[{}]
	return ans

def location(query):
        ans="<NA>"
        
        import locentric as location
        ans = location.main(query)
	if ans :
           ans=[{"location":ans}]
	#print ans
	return ans



def exam(query):
        ans="<NA>"
        import exam
	
        ans = exam.main(query)
	#print ans
        if ans :
           ans=[{"exam":ans}]
        return ans


def movie(query,orig_query):
	ans="<NA>"
	import movieretrieve1 as mv
	ans = mv.new_movies(query)
	if ans :
	   ans[0]={"movie":ans[0]}
	#else:
	   #import movie_old
	   #ans = movie_old.movie(query,orig_query)
	return ans 
	
def train(query):
	ans = "<NA>"
        import train
        ans = list(train.main(query))
        #print ans
        if ans:
           ans={"train":ans}
        #print ans
	return [ans]

def weather(query):
        import weatherRetriv as wr
        
	ans = "<NA>"
	ans=wr.queryRetriv(query)
	#print ans
	if ans.has_key('time'):
		ans.pop('time')
	if ans.has_key('id'):
		ans.pop('id')
	
	
	return [{"weather":ans}]

def stock(query):
	import stockRetriv as sr
	ans = "<NA>"
	ans= sr.getResults(query)
	if ans:
	   ans[0]={"stock":ans[0]}
	return ans

def mineral(query):
	import GSOPA as gp
	ans = list(gp.main(query))
	#print "here"
	if ans:
		ans[0]={"minerals":ans[0]}
	return ans

def sports(query):
	ans = "<NA>"
	
	import score 
	
	ans= score.scoreRetriv(query)
	if ans:
	   ans[0]={"sports":ans[0]}
	return ans

