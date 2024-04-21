from SPARQLWrapper import SPARQLWrapper, JSON

# update_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/magneto_inst/update'
# update_endpoint = 'http://10.5.0.204:3030/magneto_inst/update'#or localhost #, auth=('magneto','M4gnetoDS1'))
update_endpoint = 'http://147.102.7.185:3030/ds/update'

##In the same way we use the appropriate command to execute an UPDATE instead of an INSERT command such as we do below

#queryString = "SELECT ?subject ?predicate ?object WHERE { ?subject <http://www.semanticweb.org/thodoris/ontologies/2020/0/test#goes> ?object }"
updateString = "PREFIX test:<http://www.semanticweb.org/thodoris/ontologies/2020/0/test#> INSERT DATA {test:thodoris test:works test:stripbar . } "
#updateString = 'INSERT DATA {GRAPH <http://www.semanticweb.org/thodoris/ontologies/2020/0/test#goes> {%s %s %s}}'  %(s,p,o)

sparql = SPARQLWrapper(update_endpoint)

sparql.setQuery(updateString)
sparql.method = 'POST'
sparql.query()
