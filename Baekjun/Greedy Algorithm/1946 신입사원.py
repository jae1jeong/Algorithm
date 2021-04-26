import sys
sys.stdin = open('input.txt','r')

t = int(input())

for _ in range(t):
    n = int(input())
    candidate = []
    for i in range(n):
        test,interview = map(int,input().split())
        candidate.append([test,interview])
    
    candidate = sorted(candidate,key=lambda x:(x[0],x[1]),reverse=True)
    print(candidate)