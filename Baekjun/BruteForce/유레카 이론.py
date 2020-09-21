import sys
import itertools

input = sys.stdin.readline


T = [int(n*(n+1)/2) for n in range(1, 46)]
eureka = [0] * 1001


for i in T:
    for j in T:
        for k in T:
            if i + j + k <= 1000:
                eureka[i+j+k] = 1

print(eureka)
