import rdflib
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
import networkx as nx
import matplotlib.pyplot as plt
import ontospy
from ontospy.ontodocs.viz.viz_html_single import *


g = ontospy.Ontospy("/home/nikospps/Project_Codes/Ontologies/thodoroula.owl#")

v = HTMLVisualizer(g) # => instantiate the visualization object
v.build('/home/nikospps/Desktop') # => render visualization. You can pass an 'output_path' parameter too
v.preview() # => open in browser
######################################################################################################################
######################################################################################################################
g = rdflib.Graph()
result = g.parse('/home/nikospps/Project_Codes/Ontologies/thodoroula.owl',format='n3')

G = rdflib_to_networkx_multidigraph(result)

# Plot Networkx instance of RDF Graph
pos = nx.spring_layout(G, scale=2)
edge_labels = nx.get_edge_attributes(G, 'r')
nx.draw_networkx_edge_labels(G, pos, labels=edge_labels)
nx.draw(G, with_labels=True)
plt.show()

print(len(g))

# Add triples using store's add method
s = g.serialize(format='n3')

print(s)

# Iterate over triples in store and print them out.
print("--- printing raw triples ---")
for s, p, o in g:
    print((s, p, o))