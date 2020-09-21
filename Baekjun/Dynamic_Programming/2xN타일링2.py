

N = int(input())
dp = []
dp.append(0)
dp.append(1)
dp.append(3)
dp.append(5)
for i in range(4,N+1):
    dp.append(dp[i-1] + dp[i-2] + dp[i-2]%10007)

print(dp[N])


