from collections import deque
n = int(input())
numbers = deque(list(map(int,input().split())))
p,cnt,LR = 0,0,[]

while len(numbers) > 1:
    left,right = numbers[0],numbers[-1]
    if p > left and p > right:break
    if p < left and p < right:
        if left < right:
            p = numbers.popleft()
            LR.append("L")        
        else:
            p = numbers.pop()
            LR.append("R")
    elif p > left and p < right:
        p = numbers.pop()
        LR.append("R")
    else:
        p = numbers.popleft()
        LR.append("L")
    cnt += 1

if len(numbers) == 1 and p < numbers[0]:
    LR.append("L")
    cnt += 1

print(cnt)
print("".join(LR))

# 풀이

lt,rt= 0,n-1
last = 0
res = ""
tmp = []
while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt]),"L"))
    if a[rt] > last:
        tmp.append((a[rt],"R"))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res += tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == "L":
            lt += 1
        else:
            rt -= 1
    tmp.clear()

print(len(res)) # 문자열 길이가 수열의 길이
print(res)
        


             