from SPARQLWrapper import SPARQLWrapper, JSON, DIGEST, GET
from Person import Person
import Distances
###############################Create Asynchronization  Method for sync Purposes########################################
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

    SELECT ?FirstName ?LastName ?ID
    WHERE {
      ?x rdf:type j.0:FusedPersons;
      	 j.0:hasPersonSurname	?LastName;
      	 j.0:hasServiceUserID	?ID;
         j.0:hasPersonFirstName ?FirstName;
    }
    """

    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results
############################################Require Till Here###########################################################
########################################################################################################################
# import json
#
# with open('magneto.json', 'w') as json_file:
#     json.dump(results,json_file)
# # print(results)
########################################################################################################################
#######################################Attempt Before Trials for Demo of 3rd of July####################################
# def query_human():
#     for result in results["results"]["bindings"]:
#         id = str(result["ID"]["value"])
#         fname = str(result["FirstName"]["value"])
#         lname = str(result["LastName"]["value"])
#
#         print("Into Fuseki DB were stored {} {} with ID:{}".format(fname, lname, id))
#
# if __name__ == '__main__':
#     query_human()
# ob1, ob = str(result["object"]["value"]).split('#',1)

# print("Subject: {}, Predicate: {}, Object:{}".format(su,pr,ob))
# print(name)
# print(secName)

# Distances.calculate_person_similarity(personList[0],personList[2])

##***For Demo Purposes on 3rd of July***##
##########/////////Querying in order to retrieve just the attritubes that are already provided///////////###############
########################################################################################################################
def query_Demo(results):
    # id = 0
    Plist = []
    for result in results["results"]["bindings"]:
        # id1, ids = str(result["ID"]["value"]).split('#', 1)#here we make two sequential splits into the str's
        # id2, id = ids.split('-', 1)
        id = str(result["ID"]["value"])
        fname = str(result["FirstName"]["value"])
        lname = str(result["LastName"]["value"])
        # id += 1
        Plist.append(Person(id,fname,lname))

        # print(fname, lname, id)
    return Plist

# personList = query_Demo()