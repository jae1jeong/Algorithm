from collections import deque

def solution(n,a,b):
    answer = 0
    dq = deque([i  for i in range(1,n+1)])
    
    while dq:

        playerA = dq.popleft()
        playerB = dq.popleft()

        if len(set((playerA,playerB,a,b))) == 2:
            answer += 1
            break
        if a in [playerA,playerB]:
            answer  += 1
            dq.append(a)
        elif b in [playerA,playerB]:
            dq.append(b)
        else:
            dq.append(playerA)

    return answer


print(solution(8, 4, 7))