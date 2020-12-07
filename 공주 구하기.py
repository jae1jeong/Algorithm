from collections import deque

n,k = map(int,input().split())
arrays = deque(list(range(1,n+1)))

# while len(arrays) > k -1 : 3번째 실패
#     for index in range(1,len(arrays)+1):
#         if index == k:
#             arrays.popleft()
#             break   
#         arrays.append(arrays.popleft())

# while len(arrays) > 1:  
#     for arr in arrays:
#         if cnt == k:
#             arrays.popleft()
#             break
#         cnt += 1
# print(arrays[0])

        
while arrays:
    for _ in range(k-1):
        arrays.append(arrays.popleft())
    arrays.popleft()
    if len(arrays) == 1:
        print(arrays[0])
        arrays.pop()

    