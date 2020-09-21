N = int(input())
cards = [0] + list(map(int, input().split()))
dp = [0 for _ in range(10001)]

for i in range(1, N+1):
    for j in range(1, i+1):
        test = i - j
        dp[i] = max(dp[i], dp[i-j]+cards[j])

print(dp[N])
