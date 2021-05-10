import sys
import heapq
#sys.stdin = open('input.txt','r')


n = int(input())
hq = []
for _ in range(n):
    num = int(input())
    heapq.heappush(hq, num)
res = 0
while len(hq) != 1:
    
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    sumVal = a+b
    res += sumVal
    heapq.heappush(hq, sumVal)    
print(res)
