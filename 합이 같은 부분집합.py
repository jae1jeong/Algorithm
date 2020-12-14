import sys
sys.stdin = open('input.txt','r')


def dfs(L,_sum):
    if _sum > total//2:
        return
    if L == n:
        if _sum == (total-_sum):
            print("YES")
            sys.exit(0)
    else:
        dfs(L+1,_sum+lst[L])
        dfs(L+1,_sum)

if __name__ == '__main__':
    n = int(input())
    lst = list(map(int,input().split()))
    total = sum(lst)
    dfs(0,0)
    print("NO")