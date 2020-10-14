""" 
Facebook Social Circles - Network Graph
Source data: http://snap.stanford.edu/data/ego-Facebook.html
Chart designed by Wesley Laurence
"""

# Import libraries
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Read dataset
F = open('facebook_combined.txt')
data = F.read().splitlines()

# Prepare data for visualization
from_node_id = []
to_node_id = []

for line in data:
    nums = line.split(' ')
    from_node_id.append(int(nums[0]))
    to_node_id.append(int(nums[1]))

# Create graph
G = nx.Graph()

# Add nodes and edges to graph
for i in range(1, len(to_node_id)):
    from_val = from_node_id[i]
    to_val = to_node_id[i]
    G.add_edge(from_val, to_val)

# List of unique nodes in graph
unique_nodes = list(pd.Series(list(G.nodes())).unique())

# Get degree of each node in network for use in color map
node_degrees = []
for i in range(len(unique_nodes)):
     node_degrees.append(G.degree[i])
        
# Create figure and axis
fig, ax = plt.subplots(figsize=(30,30))
ax.set_title('Facebook Social Circles', fontsize=55)
ax.set_facecolor('whitesmoke')
ax.text(-.4, -.75, r"DATA SOURCE: Stanford Large Network Dataset Collection", fontsize=30,color='grey')

# Plot network
nx.draw(G, 
        ax=ax,
        with_labels=False,
        node_size=45,
        width=.19,
        
        # Edges
        edge_color='gray',
        style='dashed',
        
        # Color Map
        node_color=node_degrees,
        cmap=plt.cm.winter,
        vmin=1,
        vmax=375)

