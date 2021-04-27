import sys
sys.stdin = open('input.txt','r')


def DFS(L,S):
    if L == m:
        for i in range(L):
            print(res[i],end=" ")
        print()
    else:
        for i in range(S,n):
            res[L] = i
            DFS(L+1,i+1)


if __name__ == "__main__":
    n,m = map(int,input().split())
    res = [0] * (m+1)
    DFS(0,1)