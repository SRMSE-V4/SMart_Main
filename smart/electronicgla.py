__author__ = 'poke19962008'
import re
def extract(query):
    query = query.split(" ")
    StrippedQuery = []
    StopWords = ["what","where","are","is","at","and","it","an","as","are","have","in","their","said","from","for","also","by","to","other","which","new","has","was","more","be","we","that","but","they","not","with","than","a","on","these","of","could","this","so","can","at","the","or","first"]     
    for word in query:
        word = word.lower()
        word = re.sub(r"(\?|!)+", "", word)  # Remove '?', '!' from the end of the word
                    
        if word not in StopWords:
            StrippedQuery.append(word)
    return StrippedQuery
