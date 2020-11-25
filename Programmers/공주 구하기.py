from collections import deque

n,k = map(int,input().split())

princes  = deque([prince for prince in range(1,n+1)])
cnt = 0
chk = 1
# while len(princes) <= 1:
#     if chk == k:
#         princes.leftpop()
#         chk = 1
#     cnt += 1
    
# print(princes)

for idx in range(len(princes)):
    if len(princes) == 1:
        break
    if chk == k:
        princes.popleft()
        chk = 1
    chk += 1

print(princes)