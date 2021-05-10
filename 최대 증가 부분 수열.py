import sys
sys.stdin = open('input.txt','r')
n = int(input())
lst = list(map(int,input().split()))
dp = [0] * (n+1)
lst = [0] +lst
ans = -1
dp[1] = 1

for i in range(2,n+1):
    _max = 0
    for j in range(i-1,0,-1):
        if lst[i] > lst[j] and dp[j] >_max:
            _max = dp[j]
    dp[i] = _max+1
    ans = max(dp[i],ans)
print(ans)
            
        
        