import sys
sys.stdin = open('input.txt','r')


def DFS(level):
    if level == n:
        for i in range(level):
            print(res[i],end=" ")
        print()
    
    else:
        for i in range(1,n+1):
            if chk[i] == 0:
                chk[i] = 1
                res[level] = i
                DFS(level+1)
                chk[i] = 0
            



if __name__ == '__main__':
    n = int(input())
    chk = [0] * (n+1)
    res = [0] * (n+1)
    DFS(0)
    