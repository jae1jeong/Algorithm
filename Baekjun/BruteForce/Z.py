

def Z(n, x, y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y+1 == Y:
            print(result)
            return
        result += 1
        if x+1 == X and y == Y:
            print(result)
            return
        result += 1
        if x+1 == X and y+1 == Y:
            print(result)
            return
        result += 1
        return
    Z(n/2, x, y)
    Z(n/2, x, y+n/2)
    Z(n/2, x+n/2, y)
    Z(n/2, x+n/2, y+n/2)
    # 특정영역을 4등분하는게 특징


result = 0
N, X, Y = list(map(int, input().split()))
Z(2**N, 0, 0)
