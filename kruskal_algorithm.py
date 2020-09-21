

'''
최소 신장 트리의 이해

Spanning Tree, 또는 신장 트리라고 부름
원래의 그래프의 모든 노드가 연결되어 있으면서 트리의 속성을 만족하는 그래프
신장트리의 조건
    + 본래의 그래프의 모든 노드를 포함해야함
    + 모든 노드가 서로 연결
    + 트리의 속성을 만족시킴(사이클이 존재하지 않음)


최소 신장 트리
Minimun Spanning Tree,MST라고 불림
가능한 Spanning Tree 중에서 간선의 가중치 합이 최소인 Spanning Tree를 칭함.
대표적인 최소 신장 트리 알고리즘
    + 크루스칼 알고리즘, 프림 알고리즘

'''


'''
크루스칼 알고리즘
무방향 가중치의 그래프
1. 모든 정점을 독립적인 집합으로 만든다.
2. 모든 간선을 비용을 기준으로 정렬하고, 비용이 작은 간선부터 양 끝의 두 정점을 비교한다.
3. 두 정점의 최상위 정점을 확인하고, 서로 다를 경우 두 정점을 연결한다.(최소 신장 트리는 사이클이 없으므로 사이클이 생기지 않도록 하는 것임)

탐욕 알고리즘을 기초로 하고 있음(당장 눈 앞의 최소 비용을 선택해서, 결과적으로 최적의 솔루션을 찾음)


'''


'''
1. Union Find 알고리즘
서로 중복되지 않은 부분집합들끼리 합치거나 혹은 연결을 했을때 사이클이 생기는지 안 생기는지 확인하는 알고리즘
노드들 중에 연결된 노드를 찾거나, 노드들을 서로 연결할 때 (합칠 때)사용
Disjoin Set(서로 중복되지 않은 집합)들로 나눠진 원소들의 정보를 저장하고 조작하는 자료구조


순서
1. 초기화
    n개의 원소가 개별 집합으로 이뤄지도록 초기화
2. Union
    두 개별 집합을 하나의 집합으로 합침, 두 트리를 하나의 트리로 만듬

3. Find
    두 노드가 동일한 부분집합이 있는지 체크(사이클 여부를 체크하는 로직)
    두 parent 노드가 같은지 다른지 비교


고려할점
Union 순서에 따라서, 최악의 경우 링크드 리스트와 같은 형태가 될 수도 있음
이 때는 Find/Union 계산량이 O(N)이 될 수 있으므로, 해당 문제를 해결하기 위해, union-by-rank,path compression 기법을 사용함


'''

'''
union-by-rank 기법
각 트리에 대해 높이(rank)를 기억해 두고, Union시 두 트리의 높이(rank)가 다르면, 높이가 작은 트리를 높이가 큰 트리에 붙임(즉,
높이가 큰 트리의 루트 노드가 합친 집합의 루트 노드가 되게 함)

높이가 동일하다면
어느쪽에 관계없이 rank를 하나 1 증가 시켜 다른 쪽의 rank를 증가시킨 노드에 합쳐준다

높이가 h-1인 트리를 만들기 위해 최소 n개의 원소가 필요하다면, 높이가 h인 트리가 만들어지기 위해서는 최소 2n개의 원소가 필요함
따라서 union-by-rank 기법을 사용하면, union/find 연산의 시간복잡도는 O(N)이 아닌, O(logN)로 낮출 수 있음
'''


'''
path compression

Find를 실행한 노드에서 거쳐간 노드를 루트에 다이렉트로 연결하는 기법
Find를 실행한 노드는 이후부터는 루트 노드를 한번에 알 수 있음



union-by-rank와 path compression 기법을 사용하면 시간 복잡도는 O(M logN) 거의 O(1)에 가깝다고 볼 수 있음 
'''


mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}


parent = dict()
rank = dict()


def make_set(node):
    # 초기화
    parent[node] = node
    rank[node] = 0


def find(node):
    # path compression 기법
    if parent[node] != node:
        parent[node] = find(parent[node])

    return parent[node]


def union(node_u, node_v):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]:
        parent[root2] = root1

    else:
        parent[root1] = root2

        if parent[root1] == parent[root2]:
            rank[root2] += 1  # 루트 노드만 랭크 + 1시키면 됨.


def kruskal(graph):
    mst = list()

    # 1. 초기화
    for node in graph["vertices"]:
        make_set(node)

    edges = graph["edges"]

    # 2. 간선  weight  기반 sorting
    edges.sort()  # 다른 정렬 알고리즘 가능 ex) 퀵 정렬, 병합 정렬

    # 3. 사이클 없는 간선 연결
    for edge in edges:
        weight, node_v, node_u = edge
        # find는 루트 노드를 찾는 함수
        if find(node_v) != find(node_u):  # 루트 노드가 다르다면 싸이클이 없다는 것 -> 유니온 |상수시간이 걸림
            union(node_v, node_u)
            mst.append(edge)

    return mst


print(kruskal(mygraph))


'''
시간 복잡도


make-set 초기화 하나씩 다 초기화해야하니까 O(N)
간선 sort 퀵소트를 사용한다면 O(N logN)이니까 O(E log E)가 됨
find와 union은 path compression과 union by rank로 O(1)
결국에는 정렬하는데 시간 복잡도를 따르게 된다.(정렬에 따라 퍼포먼스가 달라질 수도 있다.)
'''
