import sys
sys.stdin = open('input.txt','r')

n,m = map(int,input().split())
arr  = []
for _ in range(n):
    arr.append(int(input()))
dp =[0] +([10001] * m)

for i in range(n):
    for j in range(arr[i],m+1):
        if dp[j-arr[i]] != 10001:
            dp[j] = min(dp[j],dp[j-arr[i]]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])