import sys


num = int(sys.stdin.readline().strip())

ropes,max_w = [],[] # ropes는 입력 받은 데이터를 받고, max_w는 계산해서 최대값을 구하기 위해 담는 변수

for _ in range(num):
    ropes.append(int(sys.stdin.readline().strip())) # ropes 입력 받음

ropes =sorted(ropes,reverse=True) # 내림차순 정렬

for i in range(0,len(ropes)):
    max_w.append(ropes[i] * (i+1)) # max_w에 ropes값들을 append 하는데 [110,70,40,35,20,5] 110 *1 ,70 * 2 ,40 * 3 ,35 *4, 20 * 5 ,5 * 6 이기 때문에

print(max(max_w)) # 최대 들 수 있는 무게 중에서 max값을 출력

# 구현은 정말 쉬운데 문제가 이해하기 어렵다.











