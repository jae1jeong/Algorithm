test_case = int(input())

dp = [1, 2, 4]
# dp[i]] = dp[i-1] + dp[i-2]  + dp[i-3]

for i in range(3, 10):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])


for _ in range(test_case):
    n = int(input())
    print(dp[n-1])
