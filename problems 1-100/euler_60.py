# Project Euler
# Problem 60

# Prime pair sets

from itertools import combinations
import networkx as nx
import sys
from itertools import combinations
sys.path.append('../')
from euler import listPrimes

def is_prime_pair(p, q):
    pq = int(str(p) + str(q))
    qp = int(str(q) + str(p))

    return pq in all_primes and qp in all_primes

target_size = 5 # size of prime pair set
largest = 10000
nodes = listPrimes(largest)
all_primes = set(listPrimes(largest**2))

G = nx.Graph()
G.add_nodes_from(nodes)

for c in combinations(nodes, 2):
    if is_prime_pair(*c):
        G.add_edge(*c)

mc = nx.find_cliques(G)

sols = [c for c in mc if len(c) == target_size]
sums = [sum(s) for s in sols]

if len(sums) == 0:
    print("No solutions found - try a higher upper limit.")
else:
    print(min(sums))