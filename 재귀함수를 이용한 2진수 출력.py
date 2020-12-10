import sys
sys.stdin = open('input.txt','r')

def dfs(x):
    if x == 0:
        return # 그냥 return이면 함수 return
    else:
        dfs(x//2)
        print(x%2,end="")


n = int(input())
dfs(n)