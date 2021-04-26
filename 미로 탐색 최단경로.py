import sys
from collections import deque
sys.stdin = open('input.txt','r')

matrix = [list(map(int,input().split())) for _ in range(7)]
dis  = [[0] * 7 for _ in range(7)]
dx,dy = [1,-1,0,0],[0,0,-1,1]
dq = deque()
dq.append((0,0))
matrix[0][0] = 1

while dq:
    queue_size = len(dq)
    for j in range(queue_size):
        x,y = dq.popleft()
        for i in range(4):
            _x = x+dx[i]
            _y = y+dy[i]
            if _x >= 0 and _y >= 0 and _x< 7 and _y < 7 and matrix[_y][_x] == 0:
                dq.append((_x,_y))
                matrix[_y][_x] = 1
                dis[_y][_x] =  dis[y][x] +1

if dis[6][6] == 0:
    dis[6][6] = -1


print(dis[6][6])
