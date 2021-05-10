import sys
sys.stdin = open('input.txt','r')

def dfs(length):
    if dp[length] > 0:
        return dp[length]

    if length == 1 or length == 2:
        return length

    else:
        dp[length] = dfs(length-1) + dfs(length-2)
        return dp[length]


n = int(input())
dp = [0] * (n+1)
dp[1] = 1
dp[2] = 2
dp[3] = 3
print(dfs(n))


