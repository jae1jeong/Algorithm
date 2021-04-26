import sys
# sys.stdin = open('input.txt','r')

n = int(input())
matrix = [list(map(int,input())) for _ in range(n)]
dx,dy = [1,-1,0,0],[0,0,1,-1]
res= []
cnt = 0

def DFS(x,y):
    global cnt
    cnt += 1
    matrix[x][y] = 0
    for i in range(4):
        xx = dx[i] +x
        yy = dy[i] +y
        if 0<=xx<n and 0<=yy<n and matrix[xx][yy] == 1:
            DFS(xx,yy)
        
    

def printMatrix():
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=" ")
        print()

for i in range(n):
    for j in range(n):
        if(matrix[i][j] == 1):
            cnt = 0
            DFS(i,j)
            res.append(cnt)

print(len(res))
for x in sorted(res):
    print(x)

