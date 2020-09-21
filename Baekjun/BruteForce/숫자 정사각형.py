N,M = map(int,input().split())
square = [list(map(int,str(input()))) for _ in range(N)]

MAX = min(N,M)
max = 0
for i in range(N):
    for j in range(M):
        for k in range(MAX):
            if i+k <N and j+k <M:
                if square[i][j] == square[i][j+k] == square[i+k][j] == square[i+k][j+k]:
                    if max < k:
                        max = k
print((max+1)*(max+1))
                    
        