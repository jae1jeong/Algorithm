def solution(n):
    nums = ["4","1","2"]
    answer = ""
    while n:
        answer = nums[n % 3] + answer
        n = n //3 - (n%3==0)
    return answer