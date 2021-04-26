import sys
from collections import deque
# sys.stdin = open('input.txt','r')


def BFS(x,y):
    global cnt
    dq = deque()
    dq.append((x,y))
    island[x][y] = 0
    visit[x][y] = 1
    while dq:
        x,y = dq.popleft()
        for i in range(8):
            _x = x+dx[i]
            _y = y+dy[i]
            if 0<=_x<n and 0<=_y<n and island[_x][_y] == 1 and visit[_x][_y] == 0:
                visit[_x][_y] = 1
                island[_x][_y] = 0
                dq.append((_x,_y))


if __name__ == "__main__":
    n = int(input())
    island = [list(map(int,input().split())) for _ in range(n)]
    dx,dy = [1,-1,0,0,1,1,-1,-1],[0,0,1,-1,-1,1,-1,1]
    visit = [[0] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if island[i][j] == 1:
                cnt += 1
                BFS(i,j)
    

    # for i in range(n):
    #     for j in range(n):
    #         print(island[i][j],end=" ")
    #     print()

    print(cnt)
