import sys
sys.stdin = open('input.txt','r')

n = int(input())
parts = sorted(list(map(int,input().split())))
m = int(input())
needs = list(map(int,input().split()))

lt,rt = 0,n-1
tf = [0] * (len(needs))
for i in range(len(needs)):
    lt,rt = 0,n-1
    while lt <= rt:
        mid = (lt+rt) // 2
        if parts[mid] == needs[i]:
            tf[i] = 1
            break
        if parts[mid] > needs[i]:
            rt = mid -1
        else:
            lt = mid + 1
for ans in tf:
    if ans:
        print("yes",end=" ")
    else:
        print("no",end=" ")


