

# bracket = input()
bracket = input()
stack = []
cnt = 0
for i in range(len(bracket)):

    if bracket[i] == "(":
        stack.append(bracket[i])
    else:
        stack.pop()
        if bracket[i-1] == "(": # 레이저일때
            cnt += len(stack)
        else: # 쇠막대기의 끝
            cnt += 1
                
print(cnt)