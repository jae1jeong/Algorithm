import sys
sys.stdin = open('input.txt','r')
direction = str(input())
cnt = 0
for i in range(97,97+8):
    cnt +=1
    if direction[0] == chr(i):
        break
knight = [int(direction[1]),cnt]
steps = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
ans = 0
for y,x in steps:
    nx,ny = x+knight[1],y+knight[0]
    if nx>8 or nx<1 or ny>8 or ny<1:
        continue
    ans+=1

print(ans)
