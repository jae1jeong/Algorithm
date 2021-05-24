from collections import deque
def solution(maps):
    dq = deque()
    n = len(maps)
    m = len(maps[0])
    dx,dy = [0,0,-1,1],[1,-1,0,0]
    dq.append((0,0))
    dis = [[-1]*m for _ in range(n)]
    visit = [[0] * m for _ in range(n)]
    dis[0][0] = 1
    while dq:

        x,y = dq.popleft()
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            if 0<=xx<n and 0<=yy<m and maps[xx][yy] == 1 and visit[xx][yy] == 0:
                visit[x][y] = 1
                dis[xx][yy] = dis[x][y] + 1
                dq.append((xx,yy))
    
    # for i in range(n):
    #     for j in range(m):
    #         print(dis[i][j],end=' ')
    #     print()

    
    return dis[n-1][m-1]



# 효율성 통과x


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
