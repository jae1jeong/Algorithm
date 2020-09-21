N = int(input())
lst = list()
for _ in range(N):
    input_data = list(map(int, input().split()))
    lst.append((input_data[0], input_data[1]))

    lst.sort()

for i in lst:
    print(i[0], i[1])
