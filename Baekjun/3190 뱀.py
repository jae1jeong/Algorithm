import sys
sys.stdin = open('input.txt','r')
from collections import deque

n = int(input())
k = int(input())
appleList = [tuple(map(int,input().split())) for _ in range(k)]
l = int(input())
dummy = deque()
board = [[0] * n for _ in range(n)]
for x,y in appleList:
    board[x-1][y-1] = 1
dirLst = []
for _ in range(l):
    x,c = map(str,input().split())
    dirLst.append((int(x),c))
x,y = 0,0
board[x][y] = 2
second = 0
dx,dy = [0,1,0,-1],[1,0,-1,0]
direction = 0
dummy.append((x,y))

while True:
    xx = x+dx[direction]
    yy = y+dy[direction]
    if 0<=xx<n and 0<=yy<n and board[xx][yy] != 2:
        if board[xx][yy] == 1 :
            board[xx][yy] = 2
            dummy.append((xx,yy))

        elif board[xx][yy] == 0:
            board[xx][yy] = 2
            dummy.append((xx,yy))            
            nx,ny = dummy.popleft()
            board[nx][ny] = 0
            
    else:
        second += 1
        print(second)
        break

    x,y = xx,yy
    second += 1
    if len(dirLst) > 0 and second == dirLst[0][0]:
        if  dirLst[0][1] == "L":
            direction = (direction-1)%4
        else:
            direction = (direction+1)%4
        dirLst.pop(0)



