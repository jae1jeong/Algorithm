import sys
sys.stdin = open('input.txt','r')

a = int(input())
b = int(input())
c = int(input())
abc = a*b*c
nums = [0] * 10
for num in str(abc):
    nums[int(num)] += 1
for ans in nums:
    print(ans)
