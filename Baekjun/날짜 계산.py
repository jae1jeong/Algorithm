E, S, M = map(int, (input().split()))

e, s, m = 1, 1, 1


for i in range(999999999999):
    if e == E and s == S and m == M:
        break
    else:
        e = (e % 15)+1
        s = (s % 28)+1
        m = (m % 19)+1
        cnt += 1

print(cnt)
