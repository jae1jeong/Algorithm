import sys
sys.stdin = open('input.txt','r')

n,m = map(int,input().split())
min_num = -1e9
for i in range(n):
    temp = list(map(int,input().split()))
    min_num = max(min_num,min(temp))
print(min_num)