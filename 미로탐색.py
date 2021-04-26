import sys
from collections import deque
# sys.stdin = open('input.txt','r')


# 시간복잡도 4^n

def DFS(x,y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
        return
    
    else:
        for i in range(4):
            _x = dx[i] + x
            _y = dy[i] + y
            if 0 <= _x <= 6 and 0 <= _y <= 6 and matrix[_y][_x] == 0:
                matrix[_y][_x] = 1
                DFS(_x,_y)
                matrix[_y][_x] = 0


if __name__ == '__main__':
    matrix = [list(map(int,input().split())) for _ in range(7)]
    dx,dy = [1,-1,0,0],[0,0,-1,1]
    dq = deque()
    dq.append((0,0))
    matrix[0][0] = 1
    cnt = 0
    DFS(0,0)
    print(cnt)

