
def checkP(pillar,bar,x,y):
    
    if y == 0:
        return True
    if x-1 >= 0 and bar[x-1][y] == 1:
        return True
    if bar[x][y] == 1:
        return True
    if y-1>= 0 and pillar[x][y-1] == 1:
        return True

    return False
    

def checkB(pillar,bar,x,y,N):
    
    if y-1 >= 0 and pillar[x][y-1] == 1:
        return True
    if  x+1<N and y-1 >= 0 and pillar[x+1][y-1] == 1:
        return True
    if x-1>=0 and x+1<N and bar[x-1][y] == 1 and bar[x+1]][y] == 1:
        return True

    return False


def solution(n, build_frame):
    answer = [[]]
    bar = [[0] * N for _ in range(N)]
    pillar = [[0] * N for _ in range(N)]
    N = n+1

    for x,y,a,b in build_frame:
        #설치
        if b == 1:
            if a == 0:
                if checkP(pillar,bar,x,y):
                    pillar[x][y] = 1

            else:
                if checkB(pillar,bar,x,y):
                    bar[x][y] = 1
        # 삭제
        else:
            if a == 0:
                c
            else:
                pass
    for i in range(N):
        for j in range(N):
            if pillar[i][j] == 1:
                answer.append([i,j,0])
            if bar[i][j] == 1:
                answer.append([i,j,1])



    return answer



n = 5 
bf = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]