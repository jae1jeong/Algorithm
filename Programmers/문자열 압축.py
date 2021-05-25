


def solution(s):
    ans = len(s)
    for i in range(1,len(s)//2+1):
        compressed = ""
        prev = s[:i]
        cnt = 1
        for j in range(i,len(s),i):
            if prev == s[j:j+i]:
                cnt += 1
            else:
                compressed += f'{cnt}{prev}' if cnt > 1 else prev
                prev = s[j:j+i]
                cnt = 1
        compressed += f'{cnt}{prev}' if cnt > 1 else prev
        ans = min(ans,len(compressed))
        print(compressed)
    return ans
            

s = "aabbaccc"
print(solution(s))