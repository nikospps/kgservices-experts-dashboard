from SPARQLWrapper import SPARQLWrapper, JSON, DIGEST, GET
from Person_Attributes import Person
import itertools
# import Distances

#############3rd of july

def asyn():
    # query_endpoint = 'http://147.102.7.169:3030/MAGNETO/query'
    # query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/MAGNETO/query'
    # query_endpoint = 'http://147.102.7.119:3030/test/query'
    # 'http://10.5.0.204:3030/magneto_model/data', auth=('magneto','M4gnetoDS1')
    # query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/MAGNETO/query'
    query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/magneto_inst/query'  # apply it to the original database
    # query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/test/query'

    sparql = SPARQLWrapper(query_endpoint)

    sparql.setCredentials("magneto", "M4gnetoDS1")  # username & password
    sparql.setMethod(GET)  # Set GET Method in order to make queries

    query = """
    prefix :      <http://www.w3.org/2002/07/owl#> 
    prefix owl:   <http://www.w3.org/2002/07/owl#> 
    prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
    prefix xsd:   <http://www.w3.org/2001/XMLSchema#> 
    prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> 
    prefix j.0:   <http://www.magneto-h2020.eu#> 

    SELECT ?ID ?Firstname ?Lastname ?Age ?Birthname ?Nickname ?MiddleName ?Birthdate ?Residence ?Address
    WHERE {
      ?ID rdf:type j.0:Person;
      OPTIONAL{?ID j.0:hasPersonFirstName ?Firstname}
      OPTIONAL{?ID j.0:hasPersonSurname	?Lastname}
      OPTIONAL{?ID j.0:hasAge ?Age}
      OPTIONAL{?ID j.0:hasPersonBirthName ?Birthname}
      OPTIONAL{?ID j.0:hasNickName ?Nickname}
      OPTIONAL{?ID j.0:hasPersonMiddleName ?MiddleName}
      OPTIONAL{?ID j.0:hasDateOfBirth ?Birthdate}
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
        id1, ids = str(result["ID"]["value"]).split('#', 1)#here we make two sequential splits into the str's
        # id2, id = ids.split('-', 1)
        # id = str(result["ID"]["value"])
        fname = str(result["Firstname"]["value"])
        lname = str(result["Lastname"]["value"])
        #Important if else attributes which must be included into the alternative attributes in order to receive as
        #input a specific number of elements
        #Check if a given key already exists in a dictionary (element) - Important
        if "MiddleName" in result:
            mname = str(result["MiddleName"]["value"])
        else:
            mname = ''
        if "Birthdate" in result:
            dbirth = str(result["Birthdate"]["value"])
        else:
            dbirth = ''
        # id += 1
        Plist.append(Person(ids,fname,lname, mname, dbirth))
        # print(fname, lname, id)
    return Plist

# personList = query_Demo()
#
# if __name__ == '__main__':
#     query_Demo()

##Loop for return/monitor different attributes of the created instances
# for p in personList:
#     print(p.firstname, p.birthname, p.dateOfBirth)
#     for i in range(len(subject)):
#     message = []
#     for i in range(len(personList)):
#         newMessage = {
#             'id': personList[i].id,  # probably without using a string, as its predefined as string
#             'firstname': personList[i].birthname,
#             'lastname': personList[i].firstname,
#             'middlename': personList[i].middlename,
#             'dateofbirth': personList[i].dateOfBirth
#         }
#         message.append(newMessage)