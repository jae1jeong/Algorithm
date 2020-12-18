import sys
sys.stdin = open('input.txt','r')

n,k = map(int,input().split())
A = sorted(list(map(int,input().split())),reverse=True)
B = sorted(list(map(int,input().split())))

for _ in range(k):
    A.pop()
    A.append(B.pop())
    A.sort(reverse=True)
    
print(sum(A))