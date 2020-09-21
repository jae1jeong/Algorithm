from collections import deque

test_case= int(input())

for _ in range(test_case):
    N,M  = map(int,input().split())
    lst = deque(list(map(int,input().split())))
    lst = deque([(val,idx) for idx,val in enumerate(lst)])
    cnt = 0
    
    while True:
        if lst[0][0] == max(lst,key=lambda x: x[0])[0]:
            cnt += 1
            if lst[0][1] == M:
                print(cnt)
                break
            else:
                lst.popleft()
        else:
            lst.append(lst.popleft())
    

