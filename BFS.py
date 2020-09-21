
'''
대표적인 그래프 탐색 알고리즘
BFS 너비 우선 탐색: 정점들과 같은 레벨에 있는 노드들(형제 노드들)을 먼저 탐색하는 방식
DFS 깊이 우선 탐색: 정점의 자식들을 먼저 탐색하는 방식

우선 그래프는 파이썬 딕셔너리로
'''

graph = {}

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(graph)


def bfs(graph: dict, first_node):
    visited, need_visit = [], []

    need_visit.append(first_node)
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited


'''

BFS
visited 큐와 need visit 두 개의 큐 활용

'''
