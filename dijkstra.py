'''
다익스트라 알고리즘 로직
첫 정점을 기준으로 연결되어 있는 정점들을 추가해 가며, 최단 거리를 갱신하는 기법
BFS와 유사
다익스트라 알고리즘의 가장 개선된 우선순위 큐를 사용하자
'''


'''
초기화 -> 2단계
'''


import heapq
queue = []

heapq.heappush(queue, [2, ])


mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1}
}


def dijkstra(graph, start):

    distance = {node: float('inf') for node in graph}
    distance[start] = 0  # 자신은 0

    queue = []
    heapq.heappush(queue, [distance[start], start])  # 초기화

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distance[current_node] < current_distance:
            continue
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distance[adjacent]:
                distance[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distance

    # 복습필요


print(dijkstra(mygraph, 'A'))


'''
시간복잡도
각 노드마다 인접한 간선들을 모두 검사하는 과정은 O(E)
모든 배열을 업데이트하여 우선순위에 넣어질때 이 과정이 일어날 수 있다
O(E)의 시간이 걸리고, O(E)개의 노드 정보에 대해 우선순위 큐를 작업은 O(logE)가 걸림
총 O(ElogE) 밑은 2
'''
