import sys
sys.stdin = open('input.txt','r')


def DFS(level,_sum,add,minus,mul,div):
    global _min,_max
    if level == n:
        _min = min(_min,_sum)
        _max = max(_max,_sum)
        return
    
    else:
        if add:
            DFS(level+1,_sum+arr[level],add-1,minus,mul,div)
        if minus:
            DFS(level+1,_sum-arr[level],add,minus-1,mul,div)
        if mul:
            DFS(level+1,_sum*arr[level],add,minus,mul-1,div)
        if div:
            DFS(level+1,int(_sum/arr[level]),add,minus,mul,div-1)


if __name__ == '__main__':
    _max,_min = -1e9,1e9
    n = int(input())
    arr = list(map(int,input().split()))
    a,m,mu,d = map(int,input().split())
    DFS(1,arr[0],a,m,mu,d)
    print(_max)
    print(_min)