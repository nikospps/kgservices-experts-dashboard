#Extracting owl format datasets from Fuseki dbs or Semantic Files into any other (preferrable)file format
from SPARQLWrapper import SPARQLWrapper, JSON, DIGEST, GET
from Person import Person
import Distances

def asyn():
    # query_endpoint = 'http://147.102.7.185:3030/MAGNETO_TEMP/query'
    # query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/magneto_inst/query'
    query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/magneto_inst/query'
    # query_endpoint = 'http://10.5.0.204:3030/magneto_inst/query'
    # query_endpoint = 'http://147.102.7.119:3030/test/query'

    sparql = SPARQLWrapper(query_endpoint)
    # sparql.setHTTPAuth(DIGEST)
    # Connect with given credentials
    sparql.setCredentials("magneto", "M4gnetoDS1")  # username & password
    sparql.setMethod(GET)  # Set GET Method in order to make queries

    # Second query
    query = """prefix :      <http://www.magneto-h2020.eu/> 
    prefix j.0: <http://www.magneto-h2020.eu#> 
    prefix owl:   <http://www.w3.org/2002/07/owl#> 
    prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
    prefix xsd:   <http://www.w3.org/2001/XMLSchema#> 
    prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> 

    SELECT DISTINCT ?subject ?predicate ?object
    WHERE {
      ?subject rdfs:label ?predicate.
      ?subject j.0:involvesActingPerson ?x;
             {?x rdfs:label ?object}         
    }
    """

    sparql.setQuery(query)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results
########################################################################################################################
###***Define the Main method 'Get Tripletes'***###
def query_1(results):
    subject = []
    predicate = []
    object = []
    for result in results["results"]["bindings"]:
        # Clean process of the uri's in order to bring them in a human-readable format
        sub1, sub = str(result["subject"]["value"]).split('#', 1)
        # pre1, pre = str(result["predicate"]["value"]).split('#', 1)#Does not include prefix
        pre = result["predicate"]["value"]
        ob = result["object"]["value"]
        if '#' in ob:
            ob1, ob = str(ob).split('#', 1)
        # sub = result["subject"]["value"]
        # pre = result["predicate"]["value"]
        else:
            pass  # do nothing
        # print("{}, {}, {}".format(sub, pre, ob))
        subject.append(sub)
        predicate.append(pre)
        object.append(ob)
        # return "{}, {}, {}".format(sub, pre, ob)
    return (subject,predicate,object)

# subject, predicate, object = query_1()
#
# query_1()
