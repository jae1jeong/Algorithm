import sys
sys.stdin = open('input.txt','r')
n,f = map(int,input().split())


def dfs(L):
    if L == f-1:
        pass
    else:
        