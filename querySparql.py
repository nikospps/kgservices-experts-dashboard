from SPARQLWrapper import SPARQLWrapper, JSON

query_endpoint = 'http://147.102.7.185:3030/ds/query'

queryString = "SELECT ?subject ?predicate ?object WHERE { ?subject <http://www.semanticweb.org/thodoris/ontologies/2020/0/test#goes> ?object }"


sparql = SPARQLWrapper('http://147.102.7.185:3030/ds/query')

sparql.setQuery(queryString)

sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    su1, su = str(result["subject"]["value"]).split('#',1)
    #pr = result["predicate"]["value"]
    ob1, ob = str(result["object"]["value"]).split('#',1)

    #print("Subject: {}, Predicate: {}, Object:{}".format(su,pr,ob))
    print("{} goes to {}".format(su,ob))