
'''
DFS 
need_visit 스택과 visited 큐, 두 개의 자료구조 생성
'''


graph = {}

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']


def dfs(graph: dict, first_node):

    need_visit, visited = [], []
    need_visit.append(first_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited


print(dfs(graph, 'A'))
