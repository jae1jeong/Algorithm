import sys
sys.stdin = open('input.txt','r')
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort(reverse=True)
for data in lst:
    print(data,end=" ")