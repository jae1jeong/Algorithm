

def solution(number, k):
    stack = []
    for num in number:
        while len(stack) > 0 and k > 0 and num > stack[-1]: # 스택에 num 보다 크거나 같을 때까지 계속 pop
            stack.pop()
            k -= 1
        stack.append(num)
    
    if k != 0: # 제거횟수를 다 사용하지 않았을때 남은 횟수만큼 슬라이싱
        stack = stack[:-k]
    return ''.join(stack)
    
    
    
solution("1231234",3)