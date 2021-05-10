import sys
sys.stdin = open("input.txt",'r')

n = int(input())
dp = [0] * (n+1)
dp[1] = 1
dp[2] = 2
for i in range(3,n+1):
    dp[i] = dp[i-2] + dp[i-1]

# print(dp[n])

# top -> bottom

def DFS(length):
    if dp[length] > 0:
        return dp[length]

    if length == 1 or length == 2:
        return length

    else:
        dp[length] = DFS(length-1) + DFS(length-2)
        return dp[length]

dp = [0] * (n+1)

print(DFS(n))


    




