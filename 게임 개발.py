import sys
sys.stdin = open('input.txt','r')

dy,dx = [0,1,0,-1],[-1,0,1,0]
n,m = map(int,input().split())
arr = [[0] * m for _ in range(n)]
x,y,direction = map(int,input().split())
maps = []
cnt = 1
arr[x][y] = 1
for _ in range(n):
    maps.append(list(map(int,input().split())))

def turn():
    global direction
    direction -= 1
    if direction < 0:
        direction = 3
    
turn_time = 0
while True:
    turn()
    nx = dx[direction] + x
    ny = dy[direction] + y
    if arr[nx][ny] == 0 and maps[nx][ny] == 0:
        arr[nx][ny] = 1
        x,y = nx,ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 이동
        if maps[nx][ny] == 0:
            x,y = nx,ny
        else:
            break
        turn_time = 0
        
        
print(cnt)