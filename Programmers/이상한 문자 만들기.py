def solution(string):

    string = list(string.split(" "))
    ans = ""
    for strangeStr in string:
        for idx in range(len(strangeStr)):
            if idx % 2 == 0:
                ans += strangeStr[idx].upper()
            else:
                ans += strangeStr[idx].lower()
        ans += " "
    
    return ans[:-1]

print(solution("try hello world"))