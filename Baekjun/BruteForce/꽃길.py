N = int(input())
G = [list(map(int,input().split())) for _ in range(N)]
dx, dy = [0,0, 0, 1,-1], [0,1, -1, 0, 0]


def chk(lst):
    ret = 0
    flow = []
    for flower in lst:
        x = flower // N # 나누면 x좌표가 된다
        y = flower % N # 나누면 y좌표가 된다

        if x == 0 or x == N-1 or y ==0 or y == N-1:
            return 10000
        for w in range(5):
            flow.append((x+dx[w],y+dy[w]))
            ret +=  G[x+dx[w]][y+dy[w]]
    
    if len(set(flow)) != 15:
        return 10000
    return ret

 

    
ans = 10000

for i in range(N*N):
    for j in range(i+1,N*N):
        for k in range(j+1,N*N):# x,y를 한자리로 나타낸다 0 1 2 3 4 5 6 ~ N*N+1
            ans = min(ans,chk([i,j,k])) 
print(ans)