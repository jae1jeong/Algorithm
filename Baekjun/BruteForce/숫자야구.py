from itertools import permutations


permu = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
flag = [True] * len(permu)

def check(one, two, three, strike, ball):

    for idx, per in enumerate(permu):
        s, b = 0, 0
        if (per[0] == one) and (per[1] == two) and (per[2] == three):
            pass

        if (per[0] == one):
            s += 1
        if (per[1] == two):
            s += 1
        if (per[2] == three):
            s += 1

        if per[0] != one and (per[0] == two or per[0] == three):
            b += 1
        if per[1] != two and (per[1] == one or per[1] == three):
            b += 1
        if per[2] != three and (per[2] == one or per[2] == two):
            b += 1

        if (strike != s or ball != b):
            flag[idx] = False


N = int(input())
for _ in range(N):
    # baseball_count.append(list(map(int, input().split())))
    count, strike, ball = map(int, input().split())
    count = list(str(count))
    check(int(count[0]), int(count[1]), int(count[2]), strike, ball)


f = [f for f in flag if f == True]
print(len(f))
