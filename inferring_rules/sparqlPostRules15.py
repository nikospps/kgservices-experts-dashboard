from SPARQLWrapper import SPARQLWrapper, JSON, DIGEST, GET
# from Person import Person
import requests
########################################################################################################################
###WE SET THE sparql1 and sparql (for query into the existing dataset & store back to it respectively##
#####################################################STEP 1#############################################################
########################################################################################################################
# query_endpoint = 'http://147.102.7.169:3030/MAGNETO/query'
# query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/MAGNETO/query'
# query_endpoint = 'http://147.102.7.119:3030/test/query'
# 'http://10.5.0.204:3030/magneto_model/data', auth=('magneto','M4gnetoDS1')
# query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/MAGNETO/query'
query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/magneto_inst/query'
# query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/test/query'

# Set the SparqlWrapper Class where the query will be executed into the Fuseki in order to retrieve back (the) saved
# rules
sparql1 = SPARQLWrapper(query_endpoint)# set the endpoint where the query will be executed into the Fuseki db for stored rules

sparql1.setCredentials("magneto", "M4gnetoDS1")  # username & password
sparql1.setMethod(GET)  # Set GET Method in order to make queries

query = """
prefix :      <http://www.magneto-h2020.eu/>
prefix j.0: <http://www.magneto-h2020.eu#>
prefix owl:   <http://www.w3.org/2002/07/owl#>
prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix xsd:   <http://www.w3.org/2001/XMLSchema#>
prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?ID
WHERE {
  ?x rdf:type j.0:inferredPersons;
  	 j.0:hasServiceUserID	?ID;
}
"""

sparql1.setQuery(query)
sparql1.setReturnFormat(JSON)
results = sparql1.query().convert()
#####################################################STEP 2#############################################################
########################################################################################################################
# update_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/test/update'#same to the above#CHECK FIRST TO TEST
update_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/magneto_inst/update'#same to the above

response = requests.get('http://localhost:5545/reasoning15') #, auth=('magneto','M4gnetoDS1'))#Check individually each rule/jar

##In the same way we use the appropriate command to execute an UPDATE instead of an INSERT command such as we do below
########################################################################################################################
# Read a remote semantic (fuseki) file with credentials

# Extracting Data in JSON format
dataL = response.json() #response.text

tableIdsNumber = len(results["results"]["bindings"])#find the existing number of the (last) id(s) into the fuseki db

def infer():
    tableIdsNumber = len(results["results"]["bindings"])
    for i in range(len(dataL)):
        ruleName = str(dataL[i]['Reasoning_Result'])
        ruleList = ruleName.split()
        sub = repr(ruleList[0])
        # sub2, sub1 = sub.split('-',1)
        # SUPER IMPORTANT: usage of repr to include single quotes during string concatenation during string construction
        # sub = repr(sub2+sub1)
        pre = repr(ruleList[1])
        obj = repr(ruleList[2])
        inferredId = str(tableIdsNumber + 1)
        print(sub, pre, obj)
    ####################################################################################################################
    # Update String/Query Creation
        string = 'PREFIX : <http://www.magneto-h2020.eu/> PREFIX j.0: <http://www.magneto-h2020.eu#> PREFIX owl: <http://www.w3.org/2002/07/owl#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> INSERT Data {j.0:inferredPerson' + inferredId + ' j.0:hasPersonFirstName ' + sub + ' . ' + 'j.0:inferredPerson' + inferredId + ' j.0:hasPersonMiddleName ' + pre + ' . ' + 'j.0:inferredPerson' + inferredId + ' j.0:hasPersonSurname ' + obj + ' . ' + 'j.0:inferredPerson' + inferredId + ' j.0:hasServiceUserID ' + inferredId + ' . ' + 'j.0:inferredPerson' + inferredId + ' rdf:type j.0:inferredPersons . }'
    ########################################################################################################################
        # string = 'PREFIX : <http://www.magneto-h2020.eu/> PREFIX j.0: <http://www.magneto-h2020.eu#> PREFIX owl: <http://www.w3.org/2002/07/owl#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> INSERT Data {j.0:InferredRule1 j.0:hasInferredRules Person-18hasModelX6 . j.0:InferredRule1 j.0:hasServiceUserID 1 . j.0:InferredRule1 rdf:type j.0:InferredRules . }'

        sparql = SPARQLWrapper(update_endpoint)

        sparql.setCredentials("magneto", "M4gnetoDS1")  # username & password
        sparql.setMethod(GET)  # Set GET Method in order to make queries

        sparql.setQuery(string)
        sparql.method = 'POST'
        sparql.query()
        tableIdsNumber = tableIdsNumber + 1
########################################################################################################################
########################################################################################################################
