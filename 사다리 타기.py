import sys
# sys.stdin = open('input.txt','r')



# 거꾸로

def DFS(x,y):
    visit[x][y] = 1
    if x == 0:
        print(y)
        return
    else:
        # 왼쪽
        if y-1>= 0 and matrix[x][y-1] == 1 and visit[x][y-1] == 0:
            DFS(x,y-1)
        #오른쪽
        elif y+1< 10 and matrix[x][y+1] == 1 and visit[x][y+1] == 0:
            DFS(x,y+1)
        else:        
            #위
            DFS(x-1,y)


if __name__ == "__main__":
    matrix = [list(map(int,input().split())) for _ in range(10)]
    dx,dy = [0,0,-1],[1,-1,0]
    visit = [[0] * 10 for _ in range(10)]
    y = -1
    for i in range(10):
        if matrix[9][i] == 2:
            y = i
    DFS(9,y)

            
            
