N,M = map(int,input().split())
castle = [list(input()) for _ in range(N)]
SECURITY = 'X'
cnt = 0
row,column = [0] * N,[0] * M
for i in range(N):
    for j in range(M):
        if castle[i][j] == SECURITY:
            row[i] = 1
            column[j] = 1

row_count = 0
for i in range(N):
    if row[i] == 0:
        row_count += 1
column_count = 0
for j in range(M):
    if column[j] == 0:
        column_count += 1

            
print(max(row_count,column_count))
