N = int(input())
t,p = [0],[0]
answer = 0
for _ in range(N):
    ip1,ip2 = map(int,input().split())
    t.append(ip1)
    p.append(ip2)
    

def dfs(day,sum):

    if day == N+1:
        global answer
        answer = max(answer,sum)
        return 
    
    if day+t[day] <= N+1:
        dfs(day+t[day],sum+p[day])

    if day+1 <= N+1:
        dfs(day+1,sum)

dfs(1,0)
print(answer)
