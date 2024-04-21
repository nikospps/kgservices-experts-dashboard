#from rdflib import Graph, Literal, URIRef
# from rdflib.plugins.stores import sparqlstore
import rdflib

g = rdflib.Graph()
#g.load('http://dbpedia.org/resource/Semantic_Web')
g.load('http://147.102.7.180:3030/ds1/data',format='n3')

len(g)

for s,p,o in g:
    print(s,p,o)

for s,p,o in g:
    print(o)

gres = g.query("""SELECT ?subject ?predicate ?object
WHERE {
  ?subject ?predicate ?object
}
LIMIT 25""")

gres1 = g.query("""
   PREFIX ab: <http://learningsparql.com/ns/addressbook#> 

   SELECT ?craigEmail
   WHERE
   { ab:craig ab:email ?craigEmail . }
""")

for row in gres1:
    print(str(row[0]))#check the index range of the tuple that was returned
    #print(row[3])

print(g.serialize())
