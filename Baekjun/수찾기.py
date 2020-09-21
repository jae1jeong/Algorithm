import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split(" ")))

N1 = int(input())

lst1 = list(map(int, input().split(" ")))

for number in lst1:
    if number in lst:
        print(1)
    else:
        print(0)
