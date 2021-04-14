import sys
# sys.stdin = open('input.txt','r')


n,m = map(int,input().split())

matrix = [[0] * n for i in range(n)]

for i in range(m):
    x,y,distance = map(int,input().split())
    matrix[x-1][y-1] = distance

for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=" ")
    print()
        