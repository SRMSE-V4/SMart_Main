import MySQLdb as m
db=m.connect("127.0.0.1","root","#srmseONserver","rig")
cur = db.cursor(m.cursors.DictCursor)
#all discarder must removed and sent as query query
#the function will return 1 array first one is the key for highlighting the particular field asked by user and dictionary of the result
def new_movies(query):
    query=query.lower().replace("movie","")
    key=[]
    a=['director','producer','writer','screenplay','based on','editor','studio','distributor','country','budget','gross','comment']
    if 'rating' in query or 'rate' in query or 'stars' in query or 'star' in query:
        query=query.replace('rating','').replace('rate','').replace('stars','').replace('star','')
        key.append('rating')
    if 'language' in query or 'languages' in query:
        query=query.replace('languages','').replace('language','')
        key.append('lang')
    if 'cinematographer' in query or 'cinematographers' in query or 'cinematography' in query:
        query=query.replace('cinematographers','').replace('cinematographer','').replace('cinematography','')
        key.append('cinematography')
    if 'cast' in query or 'actor' in query or 'actors' in query or 'actress' in query or 'actresses' in query :
        query=query.replace('actors','').replace('actor','').replace('actress','').replace('actresses','').replace('cast','')
        key.append('cast')
    
    if 'music' in query or 'music directors' in query or 'music director' in query :
        query=query.replace('music','').replace('music directors','').replace('music director','')
        key.append('music')

    for s in a:
        if s in query:
            query=query.replace(s,'')
            key.append(s)
    query=query.replace('\n','').replace('\t','').replace('\r','').replace('  ','').strip()
    query=query.replace(' ','%')
    try:
        sql=""" select * from movies where name like '%"""+query+"""%' """
        
	cur.execute(sql)
        res=cur.fetchone()
        
    except Exception as x:
        res=' '
    if res==None:
	res=' '
    res['listKey']=key 	
    return [res]

