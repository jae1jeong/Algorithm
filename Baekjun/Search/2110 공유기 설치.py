import sys
sys.stdin = open('input.txt','r')
n,c = map(int,input().split())
homes = []
for _ in range(n):
    homes.append(int(input()))
homes.sort()

lt = 1
rt = homes[-1] -homes[0]
res = 0

while lt <= rt:
    mid =  (lt+rt) // 2
    bef = homes[0]
    cnt = 1
    for i in range(1,len(homes)):
        if homes[i] >= bef+mid:
            cnt += 1
            bef = homes[i]

    if cnt >= c:
        lt = mid+1
        res = mid
    else:
        rt = mid -1

print(res)
