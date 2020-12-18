import sys
#sys.stdin = open('input.txt','r')

def dfs(L,res):
    global cnt
    if L == n:
        temp = 0
        for v in visit:
            if v:
                res //= coins[v-1] + (res % coins[v-1])
                temp +=1
                if temp > cnt:
                    return
        cnt = min(temp,cnt)
        return
    else:
        for i in range(1,len(visit)):
            visit[L] = i
            dfs(L+1,res)
            visit[L] = 0




n = int(input())
coins = list(map(int,input().split()))
money = int(input())
visit = [0] * (n+1)
cnt = 1e9
dfs(0,money)
print(cnt)
