

from random import *


rand_data_list = list()
for num in range(10):
    rand_data_list.append(randint(1, 100))


def sequential(data_list: list, search_data: int):

    for index in range(len(data_list)):
        if data_list[index] == search_data:
            return index

    return False


print(rand_data_list)
print(sequential(rand_data_list, 17))
