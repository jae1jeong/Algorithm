import sys
sys.stdin = open('input.txt','r')

n = int(input())
string = input()
cnt = 0
for num in str(string):
    cnt += int(num)
print(cnt)