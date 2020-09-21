import sys
sys.setrecursionlimit(10000)
T = int(input())
dx,dy = [1,0,-1,0],[0,1,0,-1]



def dfs(x,y):
    ck[x][y] = 1
    for idx in range(4):
        xx,yy = x+dx[idx],y+dy[idx]
        if matrix[xx][yy] == 0 or ck[xx][yy]: # 0이거나 갔던 곳일때는 패스
            continue
        dfs(xx,yy)



for _ in range(T):
    M,N,K = map(int,input().split())
    matrix = [[0 for _ in range(50+2)] for _ in range(50+2)]
    ck = [[0 for _ in range(50+2)] for _ in range(50+2)]

    for _ in range(K):
        x,y  = map(int,input().split())
        matrix[y+1][x+1] = 1
    ans = 0
    for i in range(1,N+1):
        for j in range(1,M+1):
            if matrix[i][j] == 0 or ck[i][j]:
                continue
            dfs(i,j)
            ans += 1
    print(ans)
        

    
