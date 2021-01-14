import sys
sys.stdin = open('input.txt','r')

def dfs(L):
    global cnt
    if L == m:
        cnt += 1
        for i in range(L):
            print(res[i],end=" ")
        print()
    else:
        for i in range(1,n+1):
            if chk[i] == 0:
                chk[i] = 1
                res[L] = i
                dfs(L+1)
                chk[i] = 0

n,m = map(int,input().split())
chk = [0] * (n+1)
res = [0] * n
cnt = 0
dfs(0)
print(cnt)