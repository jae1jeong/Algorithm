import sys
sys.stdin = open('input.txt','r')
n = int(input())
lst = list(map(int,input().split()))
dp = [0] *(n)
dp[0] = lst[0]
dp[1] = max(lst[0],lst[1])

for i in range(2,n):
    dp[i] = max(dp[i-1],dp[i-2]+lst[i])

print(dp[n-1])