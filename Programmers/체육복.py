
def solution(n: int, lost: list, reserve: list):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    for index in _reserve:

        if len(_lost) == 0:
            return n-len(_lost)

        if index+1 in lost:
            _lost.remove(index+1)

        elif index-1 in lost:
            _lost.remove(index-1)

    return n - len(_lost)


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(3, [3], [1]))
# print(solution(5, [2, 4], [1, 3, 5]))
