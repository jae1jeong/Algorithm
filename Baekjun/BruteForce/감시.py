N,M = map(int,input().split())
min_val  = 1e9
visit = [[False for _ in range(M)] for _ in range(N)]
cache,board = [],[]
for i in range(N):
    board.append(list(map(int,input().split())))
    for j in range(len(board[i])):
        if board[i][j] not in [0,6]: # 벽과 0을 제외
            cache.append((i,j))

import copy
from itertools import combinations
cache_combs = list(combinations(cache,len(cache)))


def dfs(board,x,y,n):
    if n == 

def wall(x,y):
    
    if board[y][x] == 6:
        return False
    return True
    

# 0 세기
def count_board(board):
    local_cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                local_cnt +=1
    return local_cnt

leve1s= [4,2,4,4,1]
for level in leve1s:
    for i in range(level):
        for c in cache:
            y,x = c
            
            nx.ny = 0,0
            copied = copy.deepcopy(board)
            while wall()
        min_val = min(min_val,count_board(copied))

        

-1