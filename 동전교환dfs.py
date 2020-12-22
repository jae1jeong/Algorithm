import sys
sys.stdin = open('input.txt','r')

def dfs(L,_sum):
    global cnt
    if L > cnt:
        return
    if _sum > money:
        return 
    if _sum == money:
        cnt = min(cnt,L)
        return
    else:
        for i in range(len(coins)):
            dfs(L+1,_sum+coins[i])




n = int(input())
coins = list(map(int,input().split()))
money = int(input())
coins.sort(reverse=True)
cnt = 1e9
dfs(0,0)
print(cnt)