import sys
sys.stdin = open('input.txt','r')

n = int(input())
traveler = list(map(int,input().split()))
cnt = 0
res = 0
for i in traveler:
    cnt += 1
    if cnt>= i:
        res+=1
        cnt = 0
print(res)