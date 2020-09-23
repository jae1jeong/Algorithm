
def solution(n):
    cnt,sumNum = 0, 0
    for num in range(1,10001):
        sumNum += num
        if sumNum == n:
            cnt += 1
            sumNum = 0
    return cnt
        

