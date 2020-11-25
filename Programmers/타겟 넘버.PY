def solution(numbers, target):
    n = len(numbers)
    cnt = 0
    def dfs(v,total):
        if v == n:
            if total == target:
                nonlocal cnt
                cnt += 1
        else:
            dfs(v+1,total+numbers[v])
            dfs(v+1,total-numbers[v])
    
    dfs(0,0)
    return cnt