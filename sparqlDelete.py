from SPARQLWrapper import SPARQLWrapper, JSON

update_endpoint = 'http://147.102.7.185:3030/ds/update'
# update_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/magneto_inst/update'

deleteString = "PREFIX test:<http://www.semanticweb.org/thodoris/ontologies/2020/0/test#> DELETE DATA {test:thodoris test:works test:stripbar . } "

sparql = SPARQLWrapper(update_endpoint)

sparql.setQuery(deleteString)
sparql.method = 'POST'
sparql.query()
