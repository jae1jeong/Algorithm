# n 전체 원소의 수 
# picked 지금까지 고른 원소들의 번호
# toPick 더 고를 원소의 수
# 일때 앞으로 toPick개의 원소를 고르는 모든 방법을 출력한다.

def pick(n,picked,toPick):
    global cnt    
    if toPick == 0:
        print(picked)
        cnt+=1
        return
    if not picked:
        smallest = 0
    else:
        smallest = picked[-1] +1    
    for next_ in range(smallest,n):
        picked.append(next_)
        pick(n,picked,toPick-1)
        picked.pop()

# pick(7,[],3)
# print(cnt)


import re


# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


# 1..islower()
# 2..isupper()
# 3..isalpha()
# 4..isnumeric()

# lowerflag = False
# upperflag = False
# numflag = False
# specailflag = False
# alpha = False
lst = [False,False,False,False,False,False]
cnt = 0

for i in user_input:
    if i.isalpha():
        if i.islower():
            lst[1] = True
        else:
            lst[2] = True
    if i.isnumeric():
        lst[3] = True
    if not i.isalnum():
        lst[5] = True

if len(user_input) >= 10:
    lst[4] = True

for l in lst:
    if l:
        cnt+=1
level = "LEVEL"+ str(cnt)
print(level)