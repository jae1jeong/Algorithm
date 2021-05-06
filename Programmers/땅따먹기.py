import sys
sys.setrecursionlimit(10**9)

def solution(land):
    answer = 0

    
    max_node = len(land)
    def DFS(level,_sum,previous_idx):
        nonlocal answer
        if level == max_node:
            answer = max(answer,_sum)
            return

        else:
            if previous_idx < 0:
                for i in range(4):
                    DFS(level+1,land[level][i]+_sum,i)
            else:
                for i in range(4):
                    if i == previous_idx:
                        continue
                    DFS(level+1,land[level][i]+_sum,i)

    DFS(0,0,-1)

    return answer




land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
land2 = [[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]
solution(land)

print(solution(land2))

# dp로 풀어야함 시간초과 나중에 다시 풀어야지


