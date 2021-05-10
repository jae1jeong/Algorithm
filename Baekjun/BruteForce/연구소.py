import sys

sys.stdin = open('input.txt',"r")

def spreadVirus(x,y):
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]

        if 0<=xx<n and 0<=yy<m and temp[xx][yy] == 0:
            temp[xx][yy] = 2
            spreadVirus(xx, yy)

def DFS(level):
    global result
    if level == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = matrix[i][j]
        
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    spreadVirus(i, j)
        
        result = max(result,checkSafeArea(temp))
        return
        
        # 바이러스 퍼지게
    else:
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][j] = 1
                    DFS(level + 1)
                    matrix[i][j] = 0
        
    return

def checkSafeArea(matrix):
    score = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                score += 1
    return score

def printMatrix(matrix):
    for i in range(n):
        for j in range(m):
            print(matrix[i][j],end=" ")
        print()

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
temp = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0  
DFS(0)
print(result)



