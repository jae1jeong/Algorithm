A,B = map(str,input().split())

cnt = 0
length = len(A)
def count(A):
    cnt = 0
    for idx in range(len(A)):
        if A[idx] != B[idx]:
            cnt += 1
    return cnt

import math
min_val = math.inf

while len(A) != len(B):
    case1 = B[0] + A
    case2 = A + B[0]
    if count(case1) > count(case2):
        A = case2
    else:
        A = case1
print(count(A))