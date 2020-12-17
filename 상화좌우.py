import sys
sys.stdin = open('input.txt','r')

n = int(input())
direction = list(map(str,input().split()))

start = [1,1]
def chk(x):
    if x > n or x<1:
        return False
    return True

for di in direction:
    if di == "R":
        if chk(start[1]+1):
            start[1] += 1
    elif di == "L":
        if chk(start[1]-1):
            start[1] -= 1
    elif di == "U":
        if chk(start[0]-1):
            start[0] -= 1
    elif di == "D":
        if chk(start[0]+1):
            start[0] += 1

for s in start:
    print(s,end=" ")