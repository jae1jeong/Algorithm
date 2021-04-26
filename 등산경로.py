import sys
# sys.stdin = open('input.txt','r')



def DFS(x,y):
    global cnt
    if x ==nx and y == ny:
        cnt += 1
        return
    else:
        for i in range(4):
            _x  = x+dx[i]
            _y = y+dy[i]
            if 0<=_x<n and 0<=_y<n and visit[_x][_y] == 0:
                if matrix[x][y] < matrix[_x][_y]:
                    visit[_x][_y] = 1
                    DFS(_x,_y)
                    visit[_x][_y] = 0
                
if __name__ == '__main__':
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    visit = [[0] * n for _ in range(n)]
    start = 1e9
    start_idx = ()
    end_idx = ()
    end = -1
    cnt = 0
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < start:
                start_idx = (i,j)
                start = matrix[i][j]
            if matrix[i][j] > end:
                end_idx = (i,j)
                end = matrix[i][j]

    nx,ny = end_idx
    x,y = start_idx
    visit[x][y] = 1
    DFS(x,y)       
    print(cnt)    
    

