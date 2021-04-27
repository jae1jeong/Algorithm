import sys
sys.stdin = open('input.txt','r')

nums = list(map(int,input()))
_sum = nums[0]
idx = 1
while idx < len(nums):
    if _sum == 1 or _sum == 0 or nums[idx]==0 or nums[idx] == 1:
        _sum += nums[idx]
    else:
        _sum *= nums[idx]
    idx += 1
        

print(_sum)

