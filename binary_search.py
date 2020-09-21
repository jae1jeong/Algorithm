

import random


def binary_search(data: list, search: int):

    if len(data) <= 1 and search == data[0]:
        return True

    if len(data) <= 1 and search != data[0]:
        return False

    if len(data) == 0:
        return False

    mid = len(data) // 2

    if data[mid] == search:
        return True
    else:
        if search > data[mid]:
            return binary_search(data[mid:], search)
        else:
            return binary_search(data[:mid], search)


data_list = random.sample(range(100), 10)
data_list.sort()
print(data_list)
print(binary_search(data_list, 10))
