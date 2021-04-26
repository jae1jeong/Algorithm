import sys
from collections import deque
# sys.stdin = open('input.txt','r')





if __name__ == "__main__":
    S,E = map(int,input().split())
    dis = [0 for i in range(10001)]
    ch = [0 for i in range(10001)]
    queue = deque()
    queue.append(S)
    ch[S] = 1
    dis[S] = 0
    while queue:
        now = queue.popleft()
        if now == E:
            break

        for next in(now-1,now+1,now+5):
            if 0 < next <10001:
                if ch[next] == 0:
                    queue.append(next)
                    ch[next] = 1
                    dis[next] = dis[now] + 1
    print(dis[E])

