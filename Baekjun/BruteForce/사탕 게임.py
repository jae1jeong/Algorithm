
def check():
    global ans
    for i in range(N):
        temp = matrix[i][0]
        cnt = 1
        for j in range(1, N):  # 가로
            if temp == matrix[i][j]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
                temp = matrix[i][j]

        temp = matrix[0][i]
        cnt = 1
        for j in range(1, N):  # 세로
            if temp == matrix[j][i]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
                temp = matrix[j][i]


N = int(input())
matrix = [list(input()) for i in range(N)]
ans = 1

for i in range(N):
    for j in range(N):
        if j+1 < N:
            if matrix[i][j] != matrix[i][j+1]:
                matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j]
                check()
                matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j]

        if i+1 < N:
            if matrix[i][j] != matrix[i+1][j]:
                matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]
                check()
                matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]
print(ans)
