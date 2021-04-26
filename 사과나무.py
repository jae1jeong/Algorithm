import sys
from collections import deque
# sys.stdin = open('input.txt','r')

n = int(input())
apple_tree = []
for _ in range(n):
    temp = list(map(int,input().split()))
    apple_tree.append(temp)

level = 0
visit = [[0] * n for _ in range(n)]
start = apple_tree[n//2][n//2]
# 방문
visit[n//2][n//2] = 1
# 동서남북
dx,dy = [1,-1,0,0],[0,0,-1,1]
_sum = start
dq = deque()
dq.append((n//2,n//2))
while dq:
    if level == n // 2:
        break
    q_size = len(dq)
    for i in range(q_size):
        y,x = dq.popleft()
        for j in range(4):
            _x = x+dx[j]
            _y = y+dy[j]
            if _x >= 0 and _y >= 0 and _x < n and _y < n:
                # 방문하지 않았다면
                if(visit[_y][_x] == 0):
                    # 방문 처리
                    visit[_y][_x] = 1
                    _sum += apple_tree[_y][_x]
                    dq.append((_y,_x))
    level += 1
print(_sum)




