
def money():
    lst = sorted(list(map(int, input().split())))

    if len(set(lst)) == 1:
        return lst[0] * 5000 + 50000

    if len(set(lst)) == 2:
        if lst[1] == lst[2]:  # 3, 1
            return 10000 + lst[1] * 1000
        else:  # 2,2
            return 2000 + (lst[1] + lst[2]) * 500

    for idx in range(3):
        if lst[idx] == lst[idx+1]:
            return 1000 + lst[i] * 100

    return lst[-1] * 100


test_case = int(input())
print(max(money() for i in range(test_case)))
