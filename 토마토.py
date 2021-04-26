import sys
from collections import deque

# sys.stdin = open('input.txt','r')

# 1 익은 토마토 0 익지 않은 토마토 -1 토마토가 들어있지 않음
n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(m)]
dq = deque()
dx,dy = [1,-1,0,0],[0,0,1,-1]
dis = [[0] * n for _ in range(m)]
cnt = -1

for i in range(m):
    for j in range(n):
        if matrix[i][j] == 1:
            dq.append((i,j))
while dq:
    x,y = dq.popleft()
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<m and 0<=yy<n and matrix[xx][yy] == 0:
            matrix[xx][yy] = 1
            dis[xx][yy] = 1 + dis[x][y]
            cnt = max(cnt,dis[xx][yy])
            dq.append((xx,yy))

flag = 1

for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            flag = -1

if not flag:
    print(flag)
else:
    print(cnt)


                        
                    





