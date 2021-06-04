# Programmers 괄호 회전하기 Level 2
from collections import deque
def solution(s):
    answer = 0
    dq = deque(s)
    bracket_dict = dict()
    bracket_dict[")"] = "("
    bracket_dict["]"] = "["
    bracket_dict["}"] = "{"
    for _ in range(len(s)):
        stk = []
        flag = True
        dq.rotate(-1)
        for bracket in dq:
            if bracket in ["(","{","["]:
                stk.append(bracket)
            else:
                if len(stk) <= 0 or bracket_dict[bracket] != stk[-1]:
                    flag = False
                    continue
                else:
                    stk.pop()
        else:
            if flag and len(stk) <= 0:
                answer += 1
    return answer