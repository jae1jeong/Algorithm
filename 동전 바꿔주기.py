import sys
# sys.stdin = open('input.txt','r')




def DFS(v,price):
    global cnt
    if price>T:
        return

    if v == k:
        if price == T:
            cnt += 1
            return
    else:
        for i in range(cn[v]+1):
            DFS(v+1,price+(cv[v]*i))
        
if __name__ == '__main__':
    T  = int(input())
    k = int(input())
    coin_lst = [0]
    cnt = 0
    cv = []
    cn = []
    for _ in range(k):
        coin,coin_count = map(int,input().split())
        cv.append(coin)
        cn.append(coin_count)

    DFS(0,0)
    print(cnt)