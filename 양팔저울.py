import sys
# sys.stdin = open('input.txt','r')



def DFS(v,_sum):
    global res
    if v == n:
        if 0<_sum<= s:
            res.add(_sum)
    else:
        DFS(v+1,_sum+G[v])
        DFS(v+1,_sum-G[v])
        DFS(v+1,_sum)




if __name__ == "__main__":
    n = int(input())
    G = list(map(int,input().split()))
    s = sum(G)
    res = set()
    DFS(0,0)
    print(s-len(res))
    