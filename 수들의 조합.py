import sys
# sys.stdin = open('input.txt','r')


def dfs(level,start,_sum):
    global cnt

    if level == k:
        if _sum % m == 0:
            cnt += 1 

    else:
        for i in range(start,n):
            dfs(level+1,i+1,_sum+nums[i])

if __name__ == "__main__":
    n,k = map(int,input().split())
    nums = list(map(int,input().split()))
    m  = int(input())
    cnt = 0
    dfs(0,0,0)
    print(cnt)

