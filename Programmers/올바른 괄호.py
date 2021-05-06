def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    

    stk  = []

    
    for brk in s:
        if brk == "(":
            stk.append("(")
        else:
            if len(stk)>0 and stk[-1] == "(":
                stk.pop()
            else:
                return False
    

    if len(stk) != 0:
        answer = False
        return answer

    return True





print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))