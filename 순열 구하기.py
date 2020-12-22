import sys
sys.stdin = open('input.txt','r')

def dfs(v):
    if v > n:
        for i in range(1,n+1):
            if res[i]:
                print(i,end=" ")
        print()
    else:
        res[v] = 1
        dfs(v+1)
        res[v] = 0
        dfs(v+1)

n,m = map(int,input().split())
res = [0] * (n+1)
dfs(1)