


bracket = list(map(str,input().split())

stack = []
cnt = 0
for i in range(len(bracket)):

    if bracket[i] == "(":
        stack.append(bracket[i])
    else:
        if bracket[i-1] == "(":
            stack.pop()
                
