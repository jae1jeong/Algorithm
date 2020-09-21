

def fibo(n: int):

    if n <= 1:
        return n

    return fibo(n-1) + fibo(n-2)

# 동적 계획법 활용


def fibo_dp(n: int):

    cache = [0 for index in range(n+1)]
    cache[0] = 0
    cache[1] = 1

    for index in range(2, n+1):
        cache[index] = cache[index-1] + cache[index-2]
    return cache[n]


print(fibo_dp(33))
