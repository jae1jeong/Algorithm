N,M = map(int,input().split())
ch = [str(input()) for _ in range(N)]
white_first,black_first= "WB" * 4,"BW" * 4
board,board1 = [],[]
min_val = 1e9
for i in range(4):
    board.append(white_first)
    board.append(black_first)
    board1.append(black_first)
    board1.append(white_first)

def chk(ch_board,x,y):
    cnt = 1e9
    board_cnt = 0
    board1_cnt = 0
    for i in range(8):
        for j in range(8):
            if ch_board[i+x][j+y] != board[i][j]: board_cnt += 1
            if ch_board[i+x][j+y] != board1[i][j]: board1_cnt += 1
    cnt = min(board1_cnt,board_cnt)
    return cnt

for i in range(N+1-8):
    for j in range(M+1-8):
        min_val = min(min_val,chk(ch,i,j))
            
# 상남자 완전탐색
# for i in range(N):
#     for j in range(M):
#         try:
#             min_val = min(min_val,chk(ch,i,j))
#         except IndexError as e:
#             pass
print(min_val)
