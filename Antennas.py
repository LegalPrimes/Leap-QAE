# Import networkx graph library
import networkx as nx

# Import dwave_networkx library for D-Wave functions
import dwave_networkx as dnx

# Import matplotlib.pyplot to draw graphs on screen
import matplotlib.pyplot as plt

# Set up the solver
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
my_sampler = EmbeddingComposite(DWaveSampler())

# Create an empty graph
G = nx.Graph()

# Add nodes and edges to the empty graph variable
G.add_edges_from([(1,2),(1,3),(2,3),(3,4),(3,5),(4,5),(4,6),(5,6),(6,7)])

# Find the maximum indepenent set, S
S = dnx.maximum_independent_set(G, sampler=my_sampler, num_reads=10)

# Print the solutions to the problem
print ('Maximum independent set size found is', len(S))
print (S)

k = G.subgraph(S)
notS = list(set(G.nodes())-set(S))
othersubgraph = G.subgraph(notS)
pos = nx.spring_layout(G)
plt.figure()
nx.draw(G, pos=pos)
nx.draw(k, pos=pos)
nx.draw(othersubgraph, pos=pos, node_color='b')
plt.show()
