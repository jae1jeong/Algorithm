import sys


num = int(sys.stdin.readline().strip())
stair = []
for _ in range(num):
    stair.append(int(sys.stdin.readline().strip()))

dp = []
dp.append(stair[0])
dp.append(stair[0]+stair[1])
dp.append(max(stair[2]+stair[0],stair[2]+stair[1]))


for i in range(3,num):
    # 직전 계단을 밟았을 경우, 직전 계단을 밟지 않았을 경우
    dp.append(max(dp[i-3]+stair[i-1]+stair[i],dp[i-2]+stair[i]))


print(dp[-1])


