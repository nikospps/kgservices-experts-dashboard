from SPARQLWrapper import SPARQLWrapper, JSON, DIGEST, GET
from geopy.geocoders import Nominatim
from Person import Person
import urllib.parse as urlparse
# import Distances
########################################################################################################################
########################################################################################################################
def asyn():
    # query_endpoint = 'http://147.102.7.169:3030/MAGNETO/query'
    # query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/MAGNETO/query'
    # query_endpoint = 'http://147.102.7.119:3030/test/query'
    # 'http://10.5.0.204:3030/magneto_model/data', auth=('magneto','M4gnetoDS1')
    # query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/MAGNETO/query'
    # query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/magneto_inst/query'
    query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/magneto_inst51e435ec-21a5-4fa1-82df-cb79d00a026c/query'
    # query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/magneto_inst362eb2cc-22d8-49d2-a94c-da4b7c0bc030/query'
    # query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/test/query'  # custom made dataset due to the umlauts problem

    sparql = SPARQLWrapper(query_endpoint)

    sparql.setCredentials("magneto", "M4gnetoDS1")  # username & password
    sparql.setMethod(GET)  # Set GET Method in order to make queries

    query = """
prefix http: <http://www.w3.org/2011/http#>
prefix :      <http://www.w3.org/2002/07/owl#> 
prefix owl:   <http://www.w3.org/2002/07/owl#> 
prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
prefix xsd:   <http://www.w3.org/2001/XMLSchema#> 
prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> 
prefix j.0:   <http://www.magneto-h2020.eu#> 

SELECT ?callernum ?calleenum ?frequency 
WHERE {
?call rdf:type j.0:TelephoneCall.
?call j.0:hasTelephoneCaller ?caller
  {?caller rdfs:label ?callernum}.
?call j.0:hasTelephoneCallee ?callee
  {?callee rdfs:label ?calleenum}.
?call j.0:hasFrequency ?frequency

}
    """

    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

def query_Demo(results):
    subject = []
    predicate = []
    object = []
    # nom = Nominatim(user_agent='http://dockerengine.magneto.dcom.upv.es:5050/')
    for result in results["results"]["bindings"]:
        # latitude, latitude1 = str(result["lat"]["value"]).split('e', 1)#here we make two sequential splits into the str's
        # longitude, longitude1 = str(result["lon"]["value"]).split('e', 1)
        # print(latitude)
        # id2, id = ids.split('-', 1)
        # id = str(result["ID"]["value"])
        # latitude = str(result["lat"]["value"])
        # longitude = str(result["lon"]["value"])
        # location = nom.reverse(latitude+","+longitude)
        # print(location.address)
        # print(latitude+","+longitude)
        caller = str(result["callernum"]["value"])
        freq = str(result["frequency"]["value"])
        calleen = str(result["calleenum"]["value"])
        subject.append(caller)
        predicate.append(freq)#location.address)
        object.append(calleen)
    return (subject,predicate,object)

# personList = query_Demo(asyn())

# results = asyn()
# sub, pre, ob = query_Demo(asyn())

