import sys
sys.stdin = open('input.txt','r')

n = int(input())
dp = [0] * 30001
cnt = 0

for i in range(2,n+1):
    dp[i] = dp[i-1]+1
    print(f'i: {i} {dp[i]}')
    if i % 2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)
    if i % 5 == 0:
        dp[i] = min(dp[i],dp[i//5]+1)
    

print(dp[n])

# 모르겠다 