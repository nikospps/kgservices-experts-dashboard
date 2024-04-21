from SPARQLWrapper import SPARQLWrapper, JSON, DIGEST, GET
from Person import Person
import Distances

# IMPORTANT ADDED Function, in order to gain and AVOID asynchronization problems
def asyn():
    # query_endpoint = 'http://147.102.7.169:3030/MAGNETO/query'
    # query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/MAGNETO/query'
    # query_endpoint = 'http://147.102.7.119:3030/test/query'
    # 'http://10.5.0.204:3030/magneto_model/data', auth=('magneto','M4gnetoDS1')
    # query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/MAGNETO/query'
    query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/magneto_inst/query'
    # query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/test/query'

    sparql = SPARQLWrapper(query_endpoint)

    sparql.setCredentials("magneto", "M4gnetoDS1")  # username & password
    sparql.setMethod(GET)  # Set GET Method in order to make queries

    query = """
    prefix :      <http://www.magneto-h2020.eu/>
    prefix j.0: <http://www.magneto-h2020.eu#>
    prefix owl:   <http://www.w3.org/2002/07/owl#>
    prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix xsd:   <http://www.w3.org/2001/XMLSchema#>
    prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?ID ?Sub ?Pre ?Obj
    WHERE {
      ?x rdf:type j.0:inferredPersons;
      	 j.0:hasServiceUserID	?ID;
         j.0:hasPersonFirstName ?Sub;
         j.0:hasPersonMiddleName ?Pre;
      	 j.0:hasPersonSurname	?Obj;
    }
    """

    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results
########################################################################################################################
# ob1, ob = str(result["object"]["value"]).split('#',1)

# print("Subject: {}, Predicate: {}, Object:{}".format(su,pr,ob))
# print(name)
# print(secName)

# Distances.calculate_person_similarity(personList[0],personList[2])

##***For Demo Purposes on 3rd of July***##
##########/////////Querying in order to retrieve just the attritubes that are already provided///////////###############
########################################################################################################################
def query_demo(results):
    subject = []
    predicate = []
    object = []
    for result in results["results"]["bindings"]:
        # Clean process of the uri's in order to bring them in a human-readable format
        # sub1, sub = str(result["subject"]["value"]).split('#', 1)
        # pre1, pre = str(result["predicate"]["value"]).split('#', 1)#Does not include prefix
        sub = result["Sub"]["value"]
        pre = result["Pre"]["value"]
        ob = result["Obj"]["value"]
        # if '#' in ob:
        #     ob1, ob = str(ob).split('#', 1)
        # sub = result["subject"]["value"]
        # pre = result["predicate"]["value"]
        # else:
        #     pass  # do nothing
        # print("{}, {}, {}".format(sub, pre, ob))
        subject.append(sub)
        predicate.append(pre)
        object.append(ob)
        # return "{}, {}, {}".format(sub, pre, ob)
    return (subject,predicate,object)

#Concatenate the subject, predicate & object of the inferred rule into a unique rule phrase
def query_phrase(subject, predicate, object):
    phraseRule = []
    for (a, b, c) in zip(subject, predicate, object):
        phrase = a + ' ' + b + ' ' + c
        phraseRule.append(phrase)
    return (phraseRule)

# rul = query_phrase()


