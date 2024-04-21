from owlready2 import *
import os

os.popen('')


onto = get_ontology("/usr/local/etc/res/Datasets/Victims.ttl").load()

#onto = get_ontology("http://test.org/onto.owl")
onto = get_ontology("http://147.102.7.185:3030/test/data").load()

onto = get_ontology("http://semanticdb.magneto.dcom.upv.es:3030/magneto_inst/data").load()
onto = get_ontology("http://10.5.0.204:3030/magneto_inst/data").load()


print(list(onto.classes()))
print(list(onto.object_properties()))
print(list(onto.data_properties()))
print(list(onto.individuals()))

#onto.classes()

onto.save(file = "rakoula", format = "rdfxml")

# with onto:
#     class Drug(Thing):
#         def take(self): print("I took a drug")
#
#     class ActivePrinciple(Thing):
#         pass
#
#     class has_for_active_principle(Drug >> ActivePrinciple):
#         python_name = "active_principles"
#
#     class Placebo(Drug):
#         equivalent_to = [Drug & Not(has_for_active_principle.some(ActivePrinciple))]
#         def take(self): print("I took a placebo")
#
#     class SingleActivePrincipleDrug(Drug):
#         equivalent_to = [Drug & has_for_active_principle.exactly(1, ActivePrinciple)]
#         def take(self): print("I took a drug with a single active principle")
#
#     class DrugAssociation(Drug):
#         equivalent_to = [Drug & has_for_active_principle.min(2, ActivePrinciple)]
#         def take(self): print("I took a drug with %s active principles" % len(self.active_principles))
#
# acetaminophen   = ActivePrinciple("acetaminophen")
# amoxicillin     = ActivePrinciple("amoxicillin")
# clavulanic_acid = ActivePrinciple("clavulanic_acid")
#
# AllDifferent([acetaminophen, amoxicillin, clavulanic_acid])
#
# drug1 = Drug(active_principles = [acetaminophen])
# drug2 = Drug(active_principles = [amoxicillin, clavulanic_acid])
# drug3 = Drug(active_principles = [])
#
# close_world(Drug)

print(list(onto.classes()))

ds1.Teacher

close_world(onto)
# Reasoning
with onto:
    rule = Imp()
    rule.set_as_rule("""ns:knows rdf:type owl:SymmetricProperty) (?s ns:knows ?o) -> (?o ns:knows ?s)""")

sync_reasoner(onto)
result = \
sync_reasoner_pellet()

print(drug1.__class__)
print(drug2.__class__)
print(drug3.__class__)

print(Teacher5.__class__)

onto.save(file = "thodor.owl", format = "rdfxml")