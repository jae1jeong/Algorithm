from collections import deque

need = str(input())
n = int(input())
for i in range(n):
    dq = deque(need)
    plan = input()
    for p in plan:
        if p in dq:
            if p != dq.popleft():
                print(f'#{i+1} NO')
                break
    else:
        if len(dq) == 0:
            print(f'#{i+1} YES')
        else:
            print(f'#{i+1} NO')
    
