'''
분할과 정복
퀵정렬의 핵심 
기준점(pivot)을 정해서 기준점보다 작은 데이터는 왼쪽 큰 데이터는 오른쪽으로 모은다.
각 왼쪽 오른쪽을 재귀용법을 사용해서 동일 함수를 호출하여 위 작업을 반복한다.
마지막은 왼쪽 + 기준점 + 오른쪽 리턴하는 것으로 마무리
퀵정렬의 속도는 피벗 위치에 의해서 결정된다. 여러가지 피벗 메카니즘이 있음
'''
import time
import random


def quick_sort(array):

    if len(array) <= 1:
        return array

    pivot = array[0]
    left = []
    right = []
    for n in range(1, len(array)):  # 0번이 기준점이니까 첫번째 인자는 1
        if pivot > array[n]:
            left.append(array[n])
        else:
            right.append(array[n])

        # pivot = 리스트끼리 더해야하기 떄문에 pivot을 []로 감싸준다.
    return quick_sort(left) + [pivot] + quick_sort(right)


start = time.time()
print(quick_sort([9, 7, 8, 5, 2, 4, 11, 15]))
print(time.time()-start)  # 5.698204040527344e-05


def pythonic_quicksort(array):

    if len(array) <= 1:
        return array

    pivot = array[0]
    left = [items for items in array if pivot > items]
    right = [items for items in array if pivot <= items]

    return pythonic_quicksort(left) + [pivot] + pythonic_quicksort(right)


start = time.time()
print(pythonic_quicksort([9, 7, 8, 5, 2, 4, 11, 15]))
print(time.time()-start)  # 2.8848648071289062e-05


'''
보통 quicksort보다 파이써닉한 quicksort가 리스트 컴프리헨션 때문에 더욱 빠르고 읽기 쉬운 장점이 있는 것 같다.

성능
    병합정렬과 유사 O(n log n)

    worst case
        맨 처음 pivot이 가장 크거나, 가장 작으면 모든 데이터를 비교하는 상황이 나온다. => O(n^)
'''
