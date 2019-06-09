#Uses python3

import sys


def add_edge(graph, vertex1, vertex2):
    if vertex1 in graph:
        graph[vertex1].append(vertex2)
    else:
        graph[vertex1] = [vertex2]

def acyclic(adj):
    return 0

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    graph = {vertex: [] for vertex in range(1, n+1)}

    for _ in range(m):
        vert1, vert2 = map(int, sys.stdin.readline().split())
        add_edge(graph, vert1, vert2)
    
    print(graph)
