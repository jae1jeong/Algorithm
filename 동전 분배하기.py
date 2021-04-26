import sys
# sys.stdin = open('input.txt','r')

def DFS(level,a,b,c):
    global res
    if level == n:
        temp = set()
        num = max(a,b,c) - min(a,b,c)
        temp.add(a)
        temp.add(b)
        temp.add(c)
        if len(temp) == 3:
            res = min(res,num)
        return
        

    else:
        DFS(level+1,a+coin_lst[level],b,c)
        DFS(level+1,a,b+coin_lst[level],c)
        DFS(level+1,a,b,c+coin_lst[level])

if __name__ == '__main__':
    n = int(input())
    res = 1e9
    coin_lst = []
    for _ in range(n):
        coin_lst.append(int(input()))
    
    DFS(0,0,0,0)
    print(res)