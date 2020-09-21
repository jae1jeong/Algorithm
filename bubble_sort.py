

import random


def bubble_sort(array: list):

    for index in range(len(array)-1):
        swap = False

        for index2 in range(len(array)-1):
            if array[index2] > array[index2+1]:
                array[index2], array[index2 +
                                     1] = array[index2+1], array[index2]  # swap
                swap = True

        if swap == False:
            break
    return array


def test_array(array: list):
    test = False
    ans = sorted(array)
    # print(f'정답:{ans}\n 버블 정렬:{array}')

    if ans == array:
        test = True
        print("테스트 통과하였습니다.")
    elif ans != array:
        print("테스트에 통과하지 못하였습니다.")


for _ in range(50):
    arr1 = random.sample(range(100), 50)
    test_array(bubble_sort(arr1))

'''
버블정렬의 핵심 순회를 데이터 길이-1만큼 한다. 
비교 횟수와 순회횟수를 잘 파악하여야한다. 
턴을 완료할때 맨 뒤에는 제일 큰 숫자가 정렬되기 때문에 비교할 필요가 없다.
'''
