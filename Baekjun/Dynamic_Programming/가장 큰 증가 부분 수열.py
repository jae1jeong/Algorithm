import copy
N = int(input())
lst = list(map(int, input().split()))
dp = copy.deepcopy(lst)  # 내용만 복사

# dp[i]: i까지 왔을때 합의 최대
# dp[i] =
for i in range(1, N):
    for j in range(i):
        if lst[i] > lst[j] and dp[i] < lst[i] + dp[j]:
            dp[i] = lst[i] + dp[j]


'''
1 0 if dp[1] = (100+1,100) == 101
2 0 if dp[2] = (2+1,2) = 3  2 1 if x
3 0 if dp[3] = (50+1,50) = 51 3 1 if x  3 2 dp[3] = (50+3)
4 0 if dp[4] = (60+1,60) = 61 41 ifx 42 dp[4] = (63, 61) = 63 43 dp[4] = (60+53,63) = 113
'''
print(max(dp))
