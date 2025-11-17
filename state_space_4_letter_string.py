from itertools import product
import networkx as nx
import matplotlib.pyplot as plt

def dup(edge_str: str) -> str:
    if len(edge_str) < 4 and edge_str + edge_str[-1] != edge_str:
        return edge_str + edge_str[-1]

def swap(edge_str: str) -> str:
    if len(edge_str) > 1 and edge_str[:-2] + edge_str[-1] + edge_str[-2] != edge_str:
        return edge_str[:-2] + edge_str[-1] + edge_str[-2]

def rot(edge_str: str) -> str:
    if len(edge_str) > 2 and edge_str[:-3] + edge_str[-1] + edge_str[-2] + edge_str[-3] != edge_str:
        return edge_str[:-3] + edge_str[-1] + edge_str[-2] + edge_str[-3]

edge_strs = [''.join(permutation) for n in range (1, 5) for permutation in product(["a", "b"], repeat = n)]

G = nx.DiGraph()

for edge_str in edge_strs:
    if dup(edge_str) is not None:
        G.add_edge(edge_str, dup(edge_str), rule = "dup")
    if swap(edge_str) is not None:
        G.add_edge(edge_str, swap(edge_str), rule = "swap")
    if rot(edge_str) is not None:
        G.add_edge(edge_str, rot(edge_str), rule = "rot")
    
rule_colors = {
    "dup": "red",
    "swap": "blue",
    "rot": "green",
}

# G.edges is a dict(edge: tuple(int, int), rule: string)
edge_colors = [rule_colors[G.edges[edge]["rule"]] for edge in G.edges()]
node_colors = ["gold" if node in ("ab", "abab") else "white" for node in G.nodes]

pos = nx.spring_layout(G, k = 11, iterations = 1000, scale = 10, method = "energy", seed = 10)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=node_colors,
    edge_color=edge_colors,
    width=2.5,
    node_size=1000,
    arrows=True,
    arrowsize=20,
    connectionstyle="arc3,rad=0.2"
)

ax = plt.gca()
ax.set_facecolor("black")

plt.axis("on")
plt.show()
