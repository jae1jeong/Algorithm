def solution(string):
    ans = True

    if len(string) not in [4,6]:
        ans = False
        return ans
    else:
        for stg in string:
            if stg.isalpha():
                ans = False
    
    return ans

print(solution("1234"))