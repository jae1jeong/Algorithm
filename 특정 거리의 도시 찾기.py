from collections import deque
import sys
sys.stdin = open('input.txt','r')

n,m,k,x = map(int,input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    index,road = map(int,input().split())
    graph[index].append(road)
chk = False
distance = [-1] * (n+1)
distance[x] = 0 # 출발 지점
q = deque([x])
while q:
    cur = q.popleft()
    
    for nextNode in graph[cur]:
        if distance[nextNode] == -1:
            distance[nextNode] = distance[cur] + 1
            q.append(nextNode)

for idx in range(1,len(distance)):
    if distance[idx] == k:
        chk = True
        print(idx)
if not chk:
    print(-1)
        



