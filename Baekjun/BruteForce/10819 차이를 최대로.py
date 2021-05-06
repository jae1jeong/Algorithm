import sys
sys.stdin = open('input.txt','r')


n = int(input())
nums = list(map(int,input().split()))
nums.sort(reverse=True)
cnt = 0
for i in range(1,n):
    cnt += (nums[i-1] + nums[i])

print(cnt)