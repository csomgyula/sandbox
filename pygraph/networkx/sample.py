import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_nodes_from(["A", "B", "C", "D", "E"])
g.add_edges_from([("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "E")])

#plt.style.use('dark_background')

#plt.figure(figsize=(8,6))
fig, ax = plt.subplots()
nx.draw(g, with_labels = True, 
                node_color = "dimgrey", node_size = 1000, 
                edge_color = "grey", 
                font_size = 16, font_weight = "bold")
#plt.gca().set_facecolor("black")   
ax.set_facecolor("black")                
fig.set_facecolor("black")             
plt.title("Network Graph using Python")
plt.show()                

"""
Refs:
https://pythonclcoding.medium.com/network-graph-using-python-a81f93033cfb
https://networkx.org/documentation/stable/install.html
https://stackoverflow.com/questions/59758133/how-to-change-the-color-of-the-background-in-a-networkx-plot
https://networkx.org/documentation/stable/install.html
"""