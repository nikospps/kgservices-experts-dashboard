from owlready2 import *
import types

# onto = get_ontology('http://147.102.7.185:3030/MAGNETO/data').load() #with or without data append in the uri
# onto = get_ontology('http://147.102.7.185:3030/family/data').load()
onto = get_ontology('http://147.102.7.185:3030/family#').load()

# Represent OWL classes & properties
print(list(onto.classes()))
print(list(onto.object_properties()))
print(list(onto.data_properties()))
print(list(onto.individuals()))

prop = onto.properties()

for i in prop:
    print(i)

onto.base_iri
namespace = onto.get_namespace('http://www.semanticweb.org/thodoris/ontologies/2020/0/family#')

# Print Metadata
print(onto.metadata)

# File the ontology graph into a path
onto.save(file='familara.owl')

# with onto:
#     #rule = Imp()
#     #rule.set_as_rule("""[ruleIsBro: (?x :hasParent ?z) (?y :hasParent ?z) -> (?x :isBrother ?y)]""")
#     rule1 = Imp()
#     rule1.set_as_rule("""[ruleIsBro: (?x :hasParent ?z) (?y :hasParent ?z) -> (?x :isBrother ?y)]""")

with onto.family:
rule = Imp()
# rule.set_as_rule(rule='Person(?x),hasParent(?x,?z),hasParent(?y,?z)->isBrother(?x,?y)')
rule.set_as_rule("""Person(?x),hasParent(?x,?z),hasParent(?y,?z)->isBrother(?x,?y)""")
close_world(onto.family)

with onto:
rule = Imp()
rule.set_as_rule(rule="""Person(?x),hasParent(?x,?z),hasParent(?y,?z)->isBrother(?x,?y)""",namespaces=[family])
close_world(onto)

def reasoning():
    return sync_reasoner_pellet()


reas = reasoning()

sync_reasoner_pellet(infer_data_property_values=True,infer_property_values=True)


def consistency():
    try:
        sync_reasoner_pellet()
        return 1

except OwlReadyInconsistentOntologyError:
return "The ontology is inconsistent"

consistency()
