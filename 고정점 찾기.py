import sys
sys.stdin = open('input.txt','r')
n = int(input())
lst = list(map(int,input().split()))
res = -1
lt = 0
rt = n-1
mid = (lt+rt) // 2
while lt <=rt:
    
    if lst[mid] == mid:
        res = mid
        break
    else:
        if lst[mid] > mid:
            rt = mid -1
            mid = (lt+rt)// 2
        else:
            lt = mid + 1
            mid = (lt+rt)//2

print(res)


