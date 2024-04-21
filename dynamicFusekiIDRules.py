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

SELECT ?FirstName ?LastName ?ID
WHERE {
  ?x rdf:type j.0:InferredRules;
  	 j.0:hasServiceUserID	?ID;
     j.0:hasInferredRules ?RuleName;
}
"""

sparql1.setQuery(query)
sparql1.setReturnFormat(JSON)
results = sparql1.query().convert()