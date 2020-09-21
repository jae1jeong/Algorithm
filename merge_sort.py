

'''
분할과 정복
병합정렬의 핵심
    리스트를 절반으로 잘라 비슷한 크기로 두 부분 리스트로 나눈다.
    각 부분 리스트를 재귀적으로 합병정렬을 이용해 정렬한다.
    두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다(합친다).


이렇게 하자
병합정렬은 두 함수로 나누자

분리시키는 함수와 그걸 병합하는 함수
하나까지 쪼개서 크기를 비교하면서 병합한다.
병합함수는 케이스를 3가지 생각하자
1) left/right가 아직 남아있을 때
2) left만 남아있을 때
3) right만 남아있을 때
left인덱스와 right인덱스를 선언하여 비교하면서 관리
'''


def Split(array: list):

    if len(array) <= 1:
        return array
    left, right = Split(array[:len(array)//2]), Split(array[len(array)//2:])
    return Merge(left, right)


def Merge(left: list, right: list):
    merged_list = []
    left_point, right_point = 0, 0

    # case1 left/right가 아직 남아있을때
    while len(left) > left_point and len(right) > right_point:

        if left[left_point] < right[right_point]:
            merged_list.append(left[left_point])
            left_point += 1
        else:
            merged_list.append(right[right_point])
            right_point += 1

    # case2 left만 남아있을때
    while len(left) > left_point:
        merged_list.append(left[left_point])
        left_point += 1

    # case3 right만 남아있을때
    while len(right) > right_point:
        merged_list.append(right[right_point])
        right_point += 1

    return merged_list


def test_array():
    import random

    random_data = random.sample(range(100), 20)
    assert(Split(random_data) == sorted(random_data))
    print("테스트 통과!")


test_array()
