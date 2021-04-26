import sys
# sys.stdin = open('input.txt','r')



def dfs(v,sum_num,time):
    global res
    if time > m:
        return
    if v == n:
        if sum_num > res:
            res = sum_num
        
    else:
        dfs(v+1,sum_num+score_lst[v],time+time_lst[v])
        dfs(v+1,sum_num,time)




if __name__ == '__main__':
    n,m = map(int,input().split())
    time_lst = [0]
    score_lst = [0]

    for _ in range(n):
        score,time = map(int,input().split())
        score_lst.append(score)
        time_lst.append(time)

    res = -1e9
    dfs(0,0,0)
    print(res)