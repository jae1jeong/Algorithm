import copy

# 3가지 형태로 모든 경우의수를 리스트에 더하게 된다.


def recursive(arr, n):

    if len(arr) == n:
        operation_list.append(copy.deepcopy(arr))
        return

    arr.append(" ")
    recursive(arr, n)
    arr.pop()

    arr.append("+")
    recursive(arr, n)
    arr.pop()

    arr.append("-")
    recursive(arr, n)
    arr.pop()


test_case = int(input())

for _ in range(test_case):
    operation_list = []
    n = int(input())
    recursive([], n-1)
    numbers = [i for i in range(1, n+1)]

    for operators in operation_list:
        string = ''
        for i in range(n-1):
            string += str(numbers[i]) + operators[i]
        string += str(numbers[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()
