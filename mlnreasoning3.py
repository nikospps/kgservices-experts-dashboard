from SPARQLWrapper import SPARQLWrapper, JSON, DIGEST, GET
# from Person import Person, Item
# import Distances

def asyn():
    # query_endpoint = 'http://147.102.7.169:3030/MAGNETO/query'
    # query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/MAGNETO/query'
    # query_endpoint = 'http://147.102.7.119:3030/test/query'
    # 'http://10.5.0.204:3030/magneto_model/data', auth=('magneto','M4gnetoDS1')
    # query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/MAGNETO/query'
    query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/magneto_inst/query'
    # query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/test/query'  # custom made dataset due to the umlauts problem

    sparql = SPARQLWrapper(query_endpoint)

    sparql.setCredentials("magneto", "M4gnetoDS1")  # username & password
    sparql.setMethod(GET)  # Set GET Method in order to make queries

    query = """
    Prefix j.0: <http://www.magneto-h2020.eu#>
    Prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    Select distinct ?fname ?name ?l ?c ?p WHERE {
    ?p j.0:isWitness ?y .
    ?p j.0:hasPersonFirstName ?fname .
    ?p j.0:hasPersonSurname ?name .
    ?rd a j.0:RelationDescription .
    ?rd j.0:hasConfidenceValue ?c .
    ?rd j.0:hasRangeInstance ?y .
    ?rd j.0:hasDomainInstance ?p .
    ?rd j.0:hasRelationName "http://www.magneto-h2020.eu#isWitness" .
    ?y rdfs:label ?l .
    filter (?fname !="Unknown") 
    }
    """

    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results
########################################################################################################################
#######################################Attempt Before Trials for Demo of 3rd of July####################################
def query_Demo(results):
    # id = 0
    first = []
    last = []
    incid = []
    conf = []
    for result in results["results"]["bindings"]:
        # id1, id = str(result["p"]["value"]).split('#', 1)#here we make two sequential splits into the str's
        # ev1, ev = str(result["y"]["value"]).split('#', 1)  # here we make two sequential splits into the str's
        # id2, id = ids.split('-', 1)
        # id = str(result["ID"]["value"])
        fname = str(result["fname"]["value"])
        lname = str(result["name"]["value"])
        inc = str(result["l"]["value"]) #incident
        pos = str(result["c"]["value"])#here we make two sequential splits into the str's
        # id += 1
        # Plist.append(Item(fname,lname,inc,pos))
        first.append(fname)
        last.append(lname)
        incid.append(inc)
        conf.append(pos)

        # print("{} {} is suspect in crime {} with a confidence value of {}".format(fname,lname,inc,pos))
    return (first,last,incid,conf)

# personList = query_Demo()