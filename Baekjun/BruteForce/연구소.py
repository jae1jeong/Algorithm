import copy


def set_wall(start,depth):
    global ans
    
    if depth == 3:
        copied = copy.deepcopy(matrix)
        for virus in virus_list:
            x,y = virus
            spread_virus(copied,x,y)

        ans = max(ans,chk(copied))

        return
    
    for i in range(start,n*m):
        x = i//m 
        y = i % m
        
        if matrix[x][y] == 0:
            matrix[x][y] = 1
            set_wall(i+1,depth+1)
            matrix[x][y] = 0


def chk(map):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if map[i][j] == 0:
                cnt += 1
    return cnt  

def spread_virus(map,x,y):
    for i in range(4):
        nx = x +dx[i] 
        ny = y +dy[i] 

        if 0 <= nx and nx < n and 0 <= ny and ny < m:
            if map[nx][ny] == 0:
                map[nx][ny] = 2
                spread_virus(map,nx,ny)

n,m = map(int,input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
virus_list = []
matrix = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            virus_list.append([i,j])

ans = 0
set_wall(0,0)
print(ans)


