
N = int(input())

peoples = []
for _ in range(N):
    height, size = map(int, input().split())
    peoples.append([height, size])


for i in peoples:

    rank = 1
    for j in peoples:

        if (i[0] != j[0]) and (i[1] != j[1]):
            if (i[0] < j[0]) and (i[1] < j[1]):
                rank += 1
    print(rank)
