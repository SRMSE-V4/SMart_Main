__author__ = 'poke19962008'

'''
    what are the features of Vostro 14 V3446?
    what are the features of Vostro 14 V3446 Notebook?
    what are the feature of Vostro 14 V3446?
    what are the features of Dell Vostro? <---- Return multiple matching results
'''

import pymongo, json
import electronicgla
key = ['feature', 'features', 'type', 'company', 'brand','specs','specification','specifications','spec']
dev=["cameras","camera","laptops","laptop","notebooks","netbooks","notebook","tvs","television","televisions"]
def main(query):
    try:
        con = pymongo.Connection(host="localhost", port=27017)
    except:
        print("Connection not successful ")
    dbh = con["kbmain"]

    query = electronicgla.extract(query)
    what = [x for x in query if x in key]
    if len(what)!=0:
    	query.remove(what[0])
    model = " ".join(query)
    if len(what)!=0:
		if what[0] in ['feature', 'features','specs','spec','specifications','specification']:
		    what = "features"
		elif what is 'type':
		    what = what[0]
		elif what in ["company", 'brand']:
		    what = "company"

    company = dbh.electronic.find_one({
                                "company": {
                                    "$regex": model.split()[0],
                                    "$options": "i"
                                }
                            }
                        ,  {
                                "company": True
                            }
    )

    if company != None:
        model = " ".join(model.split()[1:])
    a=model.split()
    for x in model.split():
    	if x in dev:
    		a.remove(x)
	model=" ".join(a)
    tuple = dbh.electronic.find({
                                    "model": {
                                        "$regex": model,
                                        "$options": "i"
                                    }
                                }
                               , {
                                    "_id": False,
                                    "model": True,
                                    "type":True,
                                    "company": True,
                                    "features":True,
                                    "img": True,
                                    "website": True
                                  })
    if tuple.count()==0:
    	ans=[{}]
    else:
		final=[]
		for i in range(tuple.count()):
		    final.append(tuple[i])
		ans=[{"electronics":[{"main-ans":final,"required-ans":what}]}]
    return ans
