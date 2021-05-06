import sys
sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10000)
def DFS(x,y,rain):
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]

        if 0<=xx<n and 0<=yy<n and spaces[xx][yy] > rain and visit[xx][yy] == 0:
            visit[xx][yy] = 1
            DFS(xx,yy,rain)

if __name__ == "__main__":
    n = int(input())
    spaces = [list(map(int,input().split())) for _ in range(n)]
    max_rain = max(map(max,spaces))
    cnt = 1
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    for i in range(0,max_rain+1):
        visit = [[0] * n for _ in range(n)]
        temp = 0
        for j in range(n):
            for k in range(n):
                if spaces[j][k] > i and visit[j][k] == 0:
                    DFS(j,k,i)
                    temp += 1
        cnt = max(temp,cnt)
    print(cnt)





    
