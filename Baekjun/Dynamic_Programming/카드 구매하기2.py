n = int(input())
p = [0]+list(map(int, input().split()))
dp = [0]*(n+1)

for i in range(1, n+1):
    min_val = 987654321
    for j in range(1, i+1):
        min_val = min(min_val, p[j]+dp[i-j])
    dp[i] = min_val

print(dp[n])
