

'''



'''


# 중복된 간선 빼도 됨
edges = [
    (7,"A","B"),
    (5,"A","D"),
    (8,"B","C"),
    (9,"B","D"),
    (7,"B","E"),
    (5,"C","E"),
    (7,"D","E"),
    (6,"D","F"),
    (8,"E","F"),
    (9,"E","G"),
    (11,"F","G")
]

from collections import defaultdict
from heapq import *

def prim(start_node,edges):
    # 
    mst = []
    adjacent_edges = defaultdict(list)
    for weight,n1,n2 in edges:
        adjacent_edges[n1].append((weight,n1,n2))
        adjacent_edges[n2].append((weight,n2,n1))#defaultdict(<class 'list'>, {'A': [(7, 'A', 'B'), (5, 'A', 'D')], 'B': [(7, 'B', 'A'), (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E')], 'D': [(5, 'D', 'A'), (9, 'D', 'B'), (7, 'D', 'E'), (6, 'D', 'F')], 'C': [(8, 'C', 'B'), (5, 'C', 'E')], 'E': [(7, 'E', 'B'), (5, 'E', 'C'), (7, 'E', 'D'), (8, 'E', 'F'), (9, 'E', 'G')], 'F': [(6, 'F', 'D'), (8, 'F', 'E'), (11, 'F', 'G')], 'G': [(9, 'G', 'E'), (11, 'G', 'F')]})
    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)#최소힙

    while candidate_edge_list:#간선이 없을때까지
        weight,n1,n2 = heappop(candidate_edge_list) # weight가 작은 데이터가 추출이 됨
        
        if n2 not in connected_nodes: # 인접정점이                     |사이클
            print(connected_nodes)
            connected_nodes.add(n2)

            mst.append((weight,n1,n2))

            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    
                    heappush(candidate_edge_list,edge)

    return mst
print(prim("A",edges))