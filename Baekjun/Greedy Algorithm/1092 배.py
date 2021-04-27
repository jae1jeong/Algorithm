-1
import sys
sys.stdin = open('input.txt','r')
n = int(input())
limit = sorted(list(map(int,input().split())),reverse=True)
m = int(input())
box_weight = sorted(list(map(int,input().split())),reverse=True)

if limit[0] < box_weight[0]:
    print(-1)
    sys.exit()

moved = [0] * len(box_weight)
cnt = 0
time = 0
box_length = len(box_weight)
idx = 0
while cnt < box_length:
    for i in range(n):
        if idx >= box_length:
            break
        if not moved[idx] and box_weight[idx] <= limit[i]:
            moved[idx] = 1
            cnt += 1
            idx += 1
    time += 1

print(time)
        
            
    




    


