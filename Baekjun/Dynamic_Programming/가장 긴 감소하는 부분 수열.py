import copy

N = int(input())
lst = list(map(int, input().split()))
dp = copy.deepcopy(lst)

for i in range(1, N+1):
    for j in range(i):
        if lst[i] < lst[j]:
            dp[i] = min(lst[i]-dp[j], dp[i])
