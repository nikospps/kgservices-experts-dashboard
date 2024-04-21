from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper('http://147.102.7.185:3030/ds/query')
# sparql.setQuery("""
#     prefix :      <http://www.magneto-h2020.eu/>
#     prefix magnetomodel: <http://www.magneto-h2020.eu#>
#     prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#     prefix owl:   <http://www.w3.org/2002/07/owl#>
#     prefix xsd:   <http://www.w3.org/2001/XMLSchema#>
#     prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#>
#
#     SELECT ?subject ?predicate ?object
#     WHERE {
#     ?subject ?predicate ?object
#     }
# """)

sparql.setQuery("""
SELECT ?subject ?predicate ?object WHERE { ?subject <http://www.semanticweb.org/thodoris/ontologies/2020/0/test#goes> ?object }
""")

sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    su1, su = str(result["subject"]["value"]).split('#',1)
    #pr = result["predicate"]["value"]
    ob1, ob = str(result["object"]["value"]).split('#',1)

    #print("Subject: {}, Predicate: {}, Object:{}".format(su,pr,ob))
    print("{} goes to {}".format(su,ob))