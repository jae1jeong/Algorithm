def solution(s):
    answer = 0
    stk = []
    for i in range(len(s)):
        if len(stk) >= 1 and stk[-1] == s[i]:
            stk.pop()
        else:
            stk.append(s[i])
    
    if len(stk) == 0:
        answer = 1
    return answer
s1 = 'baabaa'
solution(s1)
s2 = 'cdcd'
solution(s2)