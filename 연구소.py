import sys
sys.stdin = open('input.txt','r')


def spreadVirus(x,y):
    
    if x < 0 or x >= n or y < 0 or y>= m or factory[x][y] != 0:
        return

    else:
        factory[x][y] = 2
        
def countZeroSpace(matrix):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                cnt += 1
    return cnt

def putWall(v):
    if v == 3:
        for i in range(len(chk_lst)):
            if chk_lst:
                print(beWall[i])
        print()
        return
    else:
        for i in range(len(chk_lst)):
            chk_lst[i] = 1
            putWall(v+1)
            chk_lst[i] = 0
        



if __name__ == '__main__':
    
    beWall = []
    n,m = map(int,input().split())
    factory = []


    # 동서남북
    dx,dy = [1,-1,0,0],[0,0,1,-1]

    for i in range(n):
        temp = list(map(int,input().split()))
        factory.append(temp)

    virus = []
    for i in range(n):
        for j in range(m):
            if factory[i][j] == 0:
                beWall.append([i,j])
            elif factory[i][j] == 2:
                for k in range(4):
                    _x = dx[k] + i
                    _y = dy[k] + j
                    spreadVirus(_x,_y) 
    chk_lst = [0] * len(beWall)
    putWall(0)
    for i in range(n):
        for j in range(m):
            print(factory[i][j],end=" ")
        print()
    
        
