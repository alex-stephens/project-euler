# Project Euler
# Problem 107

# Minimal network

import networkx 

data = []

with open('euler_107.txt') as f:
    for line in f.readlines():
        data.append(line.strip().split(','))

n = len(data)
vertices = [x for x in range(n)]

G = networkx.Graph()
G.add_nodes_from(vertices)
total_weight = 0

for i in range(n):
    for j in range(i):
        if data[i][j] == '-':
            continue
        weight = int(data[i][j])
        total_weight += weight
        G.add_edge(i, j, weight=weight)

t = networkx.minimum_spanning_tree(G, weight='weight')

MST_weights = networkx.get_edge_attributes(t, 'weight')
reduced_weight = sum(MST_weights.values())

print(total_weight - reduced_weight)
