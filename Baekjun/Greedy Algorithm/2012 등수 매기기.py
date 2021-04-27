
import sys
sys.stdin = open('input.txt','r')


n = int(input())
lst = [0]
for _ in range(n):
    lst.append(int(input()))
ans = 0
lst.sort()
for i in range(1,len(lst)):
    if i != lst[i]:
        ans += abs(i-lst[i])
print(ans)
