
def multiple(n):
    if n == 1:
        return n
    return n * multiple(n-1)


string1 = "motor"

string1 = "".join(list(string1[::-1]))


def solution(n: int):
    print(n)
    if n % 2 == 0:
        return (solution(int(n/2)))

    elif n == 1:
        return n

    else:
        return (solution(int(n*3)+1))


def func(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4
    return func(data-1) + func(data-2) + func(data-3)


print(func(5))
