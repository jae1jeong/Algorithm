import sys
sys.stdin = open('input.txt','r')

S = input()

for i in range(len(S)):
    if S[i] == 0:
        S[i] = 1
    else:
        S[i] = 0

