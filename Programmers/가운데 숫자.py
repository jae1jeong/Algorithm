
def solution(s):
    list(s)
    answer = []
    if len(s) % 2 == 0:
        for i in range((len(s)//2)-1,(len(s)//2)+1):
            answer.append(s[i])
    else:
        answer.append(s[len(s)//2])
    ans = ''
    for i in answer:
        ans += str(i)

    return ans
        
        




s = 'qwer'
#print(len(s)//2)
print(solution(s))
