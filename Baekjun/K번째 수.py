from .baekjoontest import Baekjoon
N, idx = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
print(lst[idx-1])



