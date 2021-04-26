import sys
# sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10**6)

def DFS(x,y,h):
    visit[x][y] = 1
    for i in range(4):
        _x = x+dx[i]
        _y = y+dy[i]
        if 0<=_x<n and 0<=_y<n and visit[_x][_y] == 0 and space[_x][_y] > h:
            DFS(_x,_y,height)

if __name__ == '__main__':
    n = int(input())
    space = [list(map(int,input().split())) for _ in range(n)]
    dx,dy= [1,-1,0,0],[0,0,1,-1]
    ans = -1
    for height in range(101):
        visit = [[0] * n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if space[i][j] >height and visit[i][j] == 0:
                    DFS(i,j,height)
                    cnt += 1
        ans = max(ans,cnt)
        if cnt == 0:
            break
    print(ans)


