import sys
sys.stdin = open('input.txt','r')

beWall = []
n,m = map(int,input().split())
factory = [[0] * m for _ in range(n)]

for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(m):
        if temp[j] == 2:
            beWall.append([i,j])
        factory[i][j] = temp[j]

def spreadVirus(x,y):
    dx,dy = [1,0,-1,0],[0,1,0,-1]
    for i in range(4):
        if x + dx[i] >= 0 and x+dx[i] < n and y+dy[i]>=0 and y + dy[i]<m:
            spreadVirus(x+dx[i],y+dy[i])
            factory[x+dx[i]][y+dy[i]] = 2


for i in range(n):
    for j in range(m):
        if factory[i][j] == 2:
            spreadVirus(i,j)

for i in range(n):
    for j in range(m):
        print(factory[i][j],end=' ')
    print()
