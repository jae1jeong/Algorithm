def solution(s):

    s = sorted(s,reverse=True)
    answer = ''
    for i in s:
        answer += i

    return answer

print(solution("Zbcdefg"))
