test_case = int(input())
for _ in range(test_case):
    M, N, X, Y = map(int, input().split())
    cnt, x, y, flag = 1, 1, 1, False
    for i in range(M*N):
        if x == X and y == Y:
            print(cnt)
            flag = True
            break
        else:
            x = (x % M) + 1
            y = (y % N) + 1

            cnt += 1
    if not flag:
        print(-1)
