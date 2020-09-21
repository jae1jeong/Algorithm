n = int(input())


def dpsolution(n):

    dp = [-1 for _ in range(1001)]
    dp[1] = 1
    dp[2] = 2
    for idx in range(3,n+1):
        dp[idx] = dp[idx-1] + dp[idx-2]

    print(dp[n] % 10007)

dpsolution(n)





