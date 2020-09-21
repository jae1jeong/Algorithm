import sys


def DFS(graph: dict, first_node):

    need_visit, visted = [], []
    cnt = 0
    need_visit.append(first_node)
    while need_visit:
        node = need_visit.pop()
        if node not in visted:
            visted.append(node)
            need_visit.extend([graph[node]])
            print(need_visit)

            cnt += 1

    return cnt


# input = sys.stdin.readline
N = int(input())

for _ in range(N):
    friends = {}
    n = int(input())
    for _ in range(n):
        input_str = str(input())

        f1 = input_str.split(" ")

        friends[f1[0]] = f1[1]
        friends[f1[1]] = f1[0]
        print(friends)
        print(DFS(friends, friends[f1[0]]))
