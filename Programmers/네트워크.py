def solution(n, computers):

    def DFS(level):
        visit[level] = 1
        if level == n:
            return

        else:
            for i in range(n):
                if level != i and computers[level][i] == 1 and visit[i] == 0:
                    DFS(i)
    
    answer = 0
    visit = [0] * (n)
    for k in range(n):
        if visit[k] == 0:
            DFS(k)
            answer += 1

    return answer


computers = [[1,1,0],[1,1,0],[0,0,1]]

n = 3
solution(n,computers)
computers = [[1,1,0],[1,1,1],[0,1,1]]
n = 3
solution(n,computers)
