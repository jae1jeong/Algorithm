import sys
sys.stdin = open('input.txt','r')
n = int(input())
for i in range(1,n+1):
    print("*"*i)