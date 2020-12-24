import sys
sys.stdin = open('input.txt','r')
n,m = map(int,input().split())
meals = list(map(int,input().split()))
lt,rt = 0,max(meals)

def _slice(num):
    cnt = 0
    for meal in meals:
        if meal > num:
            cnt += meal-num
    return cnt
res = 0

while lt <= rt:
    mid = (lt+rt)//2
    slice_meal = _slice(mid)
    if slice_meal >= m:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)