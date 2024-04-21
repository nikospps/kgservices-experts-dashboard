from SPARQLWrapper import SPARQLWrapper, JSON, GET
import requests
########################################################################################################################
# update_endpoint = 'http://147.102.7.185:3030/ds/update'
# update_endpoint = 'http://147.102.7.169:3030/MAGNETO/update'
# update_endpoint = 'http://localhost:3030/MAGNETO/update' #used for any possible network
# update_endpoint = 'http://localhost:3030/magneto_inst/update'#same to the above
update_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/magneto_inst/update'
# update_endpoint = 'http://10.5.0.204:3030/magneto_inst/update'#or localhost #, auth=('magneto','M4gnetoDS1'))
# update_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/test/update'#same to the above

##In the same way we use the appropriate command to execute an UPDATE instead of an INSERT command such as we do below
########################################################################################################################
# Read a remote semantic (fuseki) file with credentials
response = requests.get('http://localhost:5545/fusedPersons') #, auth=('magneto','M4gnetoDS1'))

# Extracting Data in JSON format
dataL = response.json() #response.text

def ins(num):
    for i in range(len(dataL)):
        if(dataL[i]['TableId']==str(num)):
            return (dataL[i])

lam = ins(3) #id equals to 3
fusedName = repr(lam['Fused_Person_Name']) #important usage of repr to include single quotes during string concatenation
fusedSurname = repr(lam['Fused_Person_Surname'])
fusedId = repr(lam['Fused_Person_id'])
########################################################################################################################
#Update String/Query Creation
string = 'PREFIX : <http://www.magneto-h2020.eu/> PREFIX j.0: <http://www.magneto-h2020.eu#> PREFIX owl: <http://www.w3.org/2002/07/owl#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> INSERT Data {j.0:FusedPerson1 j.0:hasPersonFirstName ' + fusedName + ' . ' +  'j.0:FusedPerson1 j.0:hasPersonSurname ' + fusedSurname + ' . ' + 'j.0:FusedPerson1 j.0:hasServiceUserID ' + fusedId + ' . ' + 'j.0:FusedPerson1 rdf:type j.0:FusedPersons . }'

########################################################################################################################
sparql1 = SPARQLWrapper(query_endpoint)# set the endpoint where the query will be executed into the Fuseki db for stored rules

sparql1.setCredentials("magneto", "M4gnetoDS1")  # username & password
sparql1.setMethod(GET)  # Set GET Method in order to make queries

sparql.setQuery(string)
sparql.method = 'POST'
sparql.query()
########################################################################################################################