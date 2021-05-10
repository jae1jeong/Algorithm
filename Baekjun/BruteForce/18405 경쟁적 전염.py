import sys
from collections import deque
sys.stdin = open('input.txt','r')
dx,dy =  [1,-1,0,0],[0,0,1,-1]
n,k = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
s,target_x,target_y = map(int,input().split())
dq = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] > 0:
            dq.append((i,j,matrix[i][j],0))
dq.sort(key=lambda x:x[2])
dq = deque(dq)
while dq:
    x,y,virus,second = dq.popleft()
    if second == s:
        break
    
    for i in range(4):
        xx = x +dx[i]
        yy = y +dy[i]
        if 0<=xx<n and 0<=yy<n and matrix[xx][yy] == 0:
            matrix[xx][yy] = virus
            dq.append((xx,yy,virus,second+1))

print(matrix[target_x-1][target_y-1])



        



