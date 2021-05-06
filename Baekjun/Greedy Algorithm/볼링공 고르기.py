import sys
sys.stdin = open('input.txt','r')

def DFS(l,s):
    global cnt
    if l == 2:
        _sum = 0
        for j in range(l):
            if res[j] >= 0:
                print(lst[res[j]],end=" ")
                _sum += lst[res[j]]
        if _sum <= m:
            cnt += 1
        print()
    else:
        for i in range(s,n):
            res[l] = i
            DFS(l+1,i+1)




if __name__ == "__main__":
    n,m = map(int,input().split())
    lst = list(map(int,input().split()))
    res = [-1] * (len(lst)+1)
    cnt = 0
    DFS(0,0)
    print(cnt)

