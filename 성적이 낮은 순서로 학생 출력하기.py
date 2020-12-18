import sys
# sys.stdin = open('input.txt','r')
n = int(input())
lst = []
for _ in range(n):
    name,score = input().split()
    lst.append((name,int(score)))

lst = sorted(lst,key=lambda x:x[1])
for data in lst:
    print(data[0],end=" ")