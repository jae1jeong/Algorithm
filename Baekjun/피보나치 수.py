
# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)


# print(fibo(int(input()))) 시간 초과


fibo = []
fibo.append(0), fibo.append(1)
N = int(input())
for i in range(2, N+1):
    fibo.append(fibo[i-1] + fibo[i-2])

print(fibo[N])
