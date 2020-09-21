N = int(input())


A = [[0 for _ in range(N+1)] for i in range(N+1)]  # N크기 만큼 2차원 행렬을 만든다.
DP = [[0 for _ in range(N+1)] for i in range(N+1)]

for i in range(1, N+1):
    tmp = list(map(int, (input().split())))  # 공백 나누어서 리스트로 인풋 원소를 받는다.
    for j in range(1, i+1):
        A[i][j] = tmp[j-1]  # A 리스트에 tmp[j-1]를 할당합니다. (j-1은 0부터 시작하기 때문에 -1)

for i in range(1, N+1):
    for j in range(1, i+1):
        DP[i][j] = max(DP[i-1][j-1], DP[i-1][j])+A[i][j]
        # DP[i][j] : i,j 도착했을 때 최댓값
        # DP[i][j] = max(DP[i-1][j-1],DP[i-1][j])+ A[i][j]

# for dp in DP:
#     print(dp)
print(max(DP[-1]))  # 가장 마지막 DP원소의 최댓값을 출력한다.
