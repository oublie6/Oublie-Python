import networkx as nx
from src.Oublie.huatu import draw_nx

G = nx.read_graphml("condensed_west_europe_delete.graphml")

draw_nx(G,10,40)