
# 계수 정렬 O(N)
import sys

input = sys.stdin.readline

N = int(input())
array = [0] * 10001

for i in range(N):
    data = int(input())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)
