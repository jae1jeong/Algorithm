

N, M = map(int, input().split(" "))


lst = list(map(int, input().split(" ")))
sum_list = []

for i in lst:
    for j in lst:
        for k in lst:
            if (i == j) or(i == k) or(j == k):
                pass
            else:
                if i + j + k <= M:
                    sum_list.append(i+j+k)


print(max(sum_list))
