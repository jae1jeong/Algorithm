import sys
sys.stdin = open('input.txt','r')

n = int(input())
coin = list(map(int,input().split())).sort()

target = 1

for x in coin:
    if target < x:
        break
    target += x

print(target)

# 그리디 너무 어렵다
    