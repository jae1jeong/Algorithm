import sys
# sys.stdin = open('input.txt','r')


def DFS(v,sum_num):
    global res

    if v == n+1:
        res = max(res,sum_num)

    else:
        if v + time_lst[v] <= n+1:
            DFS(v+time_lst[v],sum_num+price_lst[v])
        DFS(v+1,sum_num) 



if __name__ == '__main__':
    n = int(input())
    time_lst = [0]
    price_lst = [0]
    res = -1

    for _ in range(n):
        time,price = map(int,input().split())
        time_lst.append(time)
        price_lst.append(price)

    DFS(1,0)
    print(res)
