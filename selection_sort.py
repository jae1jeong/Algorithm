

def selection_sort(array: list):

    for stand in range(len(array)-1):
        lowest = stand
        for index in range(stand+1, len(array)):
            if array[lowest] > array[index]:
                lowest = index  # 제일 작은 값을 찾는 과정 lowest에 담아둬서 다른 원소들이랑 비교
        array[stand], array[lowest] = array[lowest], array[stand]  # swap

    return array
