import sys
# sys.stdin = open('.\input.txt','r')

# s = input()
s = "aaaabbababb"

def solution(s):
    ans = len(s)
    
    for step in range(1,len(s)//2+1):
        prev = s[:step]
        compression = ""
        cnt = 1
        for j in range(step,len(s),step):
            if prev == s[j:j+step]:
                cnt += 1
            else:
                compression += str(cnt) + prev if cnt > 1 else prev
                cnt = 1
                prev = s[j:j+step]
            print(j)
        print(f'{cnt},{prev},{compression}')
        compression += str(cnt) + prev if cnt > 1 else prev
        ans = min(ans,len(compression))
    return ans

print(solution(s))

                
