import sys
sys.stdin = open('input.txt','r')

n,k = map(int,input().split())
cnt= 0
while n >= k:    
    while n % k == 0:
        n  = n // k
        cnt += 1
        if n == 1:
            print(cnt)
            sys.exit(0)
    n -= 1
    cnt += 1

print(cnt)

