import sys
#sys.stdin = open('input.txt','r')

def dfs(L,_sum,t_sum):
    global max_weight
    if _sum + (total-t_sum) < max_weight:
        return
    if _sum > c:
        return
    if L == n: 
        max_weight = max(_sum,max_weight)
    
    else:
        dfs(L+1,_sum+dogs[L],t_sum+dogs[L])
        dfs(L+1,_sum,t_sum+dogs[L])


if __name__ == '__main__':
    max_weight = 0
    c,n = map(int,input().split())
    dogs = []
    for _ in range(n):
        dogs.append(int(input()))
    total = sum(dogs)
    dfs(0,0,0)
    print(max_weight)