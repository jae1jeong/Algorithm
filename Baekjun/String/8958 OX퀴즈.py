import sys
sys.stdin = open('input.txt','r')
n = int(input())
for _ in range(n):
    ox = input()
    cnt = 0
    score = 0
    for i in range(len(ox)):
        if ox[i] == "O":
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)
