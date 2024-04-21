######## Approach by using 'requests' library
# import requests
#
# response = requests.post('http://147.102.7.180:3030/ds/sparql',
#        data={'query': 'ASK { ?s ?p ?o . }'})
#
# print(response.json())

from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, Literal, URIRef
from rdflib.plugins.stores import sparqlstore
import rdflib

g = rdflib.Graph()
result = g.parse('http://147.102.7.138:3030/magneto',format='n3')
print(len(g))

for subj, pred, obj in g:
    print(obj)

#g.load('http://147.102.7.180:3030/ds1/data',format='n3')

query_endpoint = 'http://147.102.7.138:3030/magneto/query'
update_endpoint = 'http://147.102.7.180:3030/magneto/update'

sparql = SPARQLWrapper("")

store = sparqlstore.SPARQLUpdateStore()

store.open((query_endpoint,update_endpoint))
# ...use store...
# store.add_graph(graph)
# store.remove_graph(graph)
# store.query(...)

# It looks like you have a turtle format file so:
#
# g = Graph(identifier = URIRef('http://www.example.com/'))
# g.parse(data=r, format='turtle')
#
# store.add_graph(g)

#store.query()
sparql = SPARQLWrapper("http://147.102.7.180:3030/ds/sparql")
#sparql = SPARQLWrapper("http://147.102.7.180:3030/ds/query")
#sparql=SPARQLWrapper("http://147.102.7.180:3030/ds/data/test")
sparql.setQuery("""
   PREFIX ab: <http://learningsparql.com/ns/addressbook#> 
   
   SELECT ?craigEmail
   WHERE
   { ab:craig ab:email ?craigEmail . }
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

#for result in results:
for result in results["results"]["bindings"]:
    print(result["label"]["value"])
    # print(result)

#sparql.setQuery()