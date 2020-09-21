R, C = map(int, input().split())
M = [list(input()) for i in range(R)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]  # 시계방향


ck = False
for i in range(R):
    for j in range(C):
        if M[i][j] == "W":
            for w in range(4):  # 시계방향으로 돈다
                ii, jj = i + dx[w], j+dy[w]
                if ii < 0 or ii == R or jj < 0 or jj == C:  # 맵 밖으로 나가버리는 경우
                    continue
                if M[ii][jj] == 'S':
                    ck = True
if ck:
    print(0)

else:
    print(1)
    for i in range(R):
        for j in range(C):
            if M[i][j] not in "SW":  # 양이나 늑대가 아닌 경우
                M[i][j] = "D"
for i in M:
    print("".join(i))
