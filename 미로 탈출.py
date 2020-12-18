import sys
from collections import deque
sys.stdin = open('input.txt','r')

n,m = map(int,input().split())
graph= []
visited = [0] * False
for _ in range(n):
    graph.append(list(map(int,input())))
dx,dy = [-1,1,0,0],[0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y= queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx >= n or ny >= m or ny < 0:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]
print(bfs(0,0))