import random


def insertion_sort(array: list):
    for index in range(len(array)-1):  # 턴이 길이-1이기 때문에  0  1 2 3 4
        for index2 in range(index+1, 0, -1):
            if array[index2] < array[index2-1]:
                array[index2], array[index2-1] = array[index2-1], array[index2]
            else:
                break

    return array


def test_array(array: list):
    test = False
    ans = sorted(array)

    if ans == array:
        test = True
        print("테스트 통과하였습니다.")
    elif ans != array:
        print("테스트에 통과하지 못하였습니다.")


if __name__ == '__main__':
    for _ in range(50):
        arr1 = random.sample(range(100), 50)
        test_array(insertion_sort(arr1))


# 핵심은  순회 횟수와 조건 비교 횟수를 패턴을 파악하여야한다.
