def split(p):
    o = 0
    c = 0
    u = ""
    for i in range(len(p)):
        if p[i] == "(":
            o += 1
        else:
            c += 1
        u += p[i]

        if o == c and o+c<len(p):
            return u,p[i+1:]
    
    return p,""


def right(p):
    stk = []
    for item in p:
        if item == "(":
            stk.append(item)
        else:
            if len(stk) == 0:
                return False
            else:
                stk.pop()
    if len(stk) == 0:
        return True
    return False

def reverse(p):
    res = ""
    for item in p:
        if item == "(":
            res += ")"
        else:
            res += "("
    return res

def solution(p):
    answer = ''
    if p == '':
        return ''
    
    u,v = split(p)
    if right(u):
        return u + solution(v)
    else:
        ans = "("
        ans = ans + v
        ans = ")"
        u = u[1:-1]
        u = reverse(u)
        return "(" + solution(v) + ")" + u
        
        




    return answer