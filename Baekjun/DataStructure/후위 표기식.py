strings = input()
stack = []
temp = ""
cal = ["*","/","+","-","(",")"]
for string in strings:
    if string.isalpha() and string not in cal:
        temp += string
    else:
        if string == "(":
            stack.append(string)
        elif string in ["*","/"]:
            while stack and (stack[-1]== "*" or stack[-1] == "/"):
                temp += stack.pop()
            stack.append(string)
        elif string in ["+","-"]:
            while stack and stack[-1] != "(": # 괄호 안에 더하기 빼기
                temp += stack.pop()
            stack.append(string)
        elif string == ")":
            while stack and stack[-1] != "(": # 연 괄호까지 있을때 까지
                temp += stack.pop()
            stack.pop() # 여는 괄호 출력하지 않고 제거
while stack: # 스택이 남아있을 수 있으니 모두 팝
    temp += stack.pop()     

print(temp)    
    