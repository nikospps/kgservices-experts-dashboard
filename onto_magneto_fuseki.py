from owlready2 import *
from rdflib import Graph
import pprint
import requests
from rdflib.plugins.sparql.results.jsonresults import JSONResultSerializer
import sys

#Script Responsible for saving locally an already stored, in fuseki, dataset, into a specific format (owl,ttl,n3)
# Read a remote semantic (fuseki) file with credentials
response = requests.get('http://semanticdb.magneto.dcom.upv.es:3030/magneto_inst/query', auth=('magneto','M4gnetoDS1'))
response = requests.get('http://10.5.0.204:3030/magneto_inst/data', auth=('magneto','M4gnetoDS1'))
# response = requests.get('http://10.5.0.204:3030/test/data', auth=('magneto','M4gnetoDS1'))
# response = requests.get('http://10.5.0.204:3030/magneto_model/data', auth=('magneto','M4gnetoDS1'))
# response = requests.get('http://147.102.7.169:3030/MAGNETO/data')
# response = requests.get('http://10.5.0.204:3030/magneto/data', auth=('magneto','M4gnetoDS1'))

n = response.text


for i in :
    print(i)


f = open('Victims.owl','w')
f.write(response.text)
f.close()
# Load the ontology from a (our) local repository
#onto = get_ontology("/home/nikospps/Project_Codes/Ontologies/thodoroula.owl").load()

#  Used if format can not be determined from source. Defaults to rdf/xml.
#  Format support can be extended with plugins, but ‘xml’, ‘n3’, ‘nt’, ‘trix’, ‘rdfa’ are built in.
g = Graph()
# g.parse("/home/nikospps/Project_Codes/Ontologies/magneto.owl",format="n3")
# g.parse("/home/nikospps/Project_Codes/Ontologies/thodoroula.owl",format="n3")
# g.parse("/home/nikospps/Projects_Codes_Development/Magneto_Ontology_Platform_Backend/magneto_model.owl",format="n3")
g.parse("/home/nikospps/Projects_Codes_Development/Magneto_Ontology_Platform_Backend/magneto_inst.owl",format="n3")

# Add triples using store's add method
#s = g.serialize(format='n3')
#print(s)

# Iterate over triples in store and print them out.
print("--- printing raw triples ---")
for s, p, o in g:
    print((s, p, o))


qres = g.query("""
    SELECT DISTINCT ?s {
        ?s ?p ?o
    }""")

JSONResultSerializer(qres).serialize(sys.stdout)