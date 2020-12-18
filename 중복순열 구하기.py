import sys
# sys.stdin = open('input.txt','r')


def dfs(v):
    global cnt
    if v == m:
        cnt += 1
        for r in res:
            if r > 0:
                print(r,end=' ')
        print()
    else:
        for i in range(1,n+1):
            res[v] = i
            dfs(v+1)
            res[v] = 0
            

if __name__ == '__main__':
    n,m = map(int,input().split())
    cnt = 0
    res = [0] * n
    dfs(0)
    print(cnt)