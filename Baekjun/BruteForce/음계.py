
lst = list(map(int, input().split(" ")))


def solution(lst):
    compare_idx = len(lst) - 1
    flag = [False] * compare_idx
    for i in range(0, len(lst)):
        if i == len(lst)-1:
            return print_answer(flag)

        if lst[i] < lst[i + 1]:
            flag[i] = True


def print_answer(flag):
    cnt = 0
    for f in flag:
        if f == True:
            cnt += 1
        elif f == False:
            pass

    if cnt == len(flag):
        print("ascending")
    elif cnt == 0:
        print("descending")
    else:
        print("mixed")


solution(lst)
