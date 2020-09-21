def solution(n):

    n = list(str(n))
    ans = 0
    for num in n:
        ans += int(num)

    return ans
        
solution(123)