N = int(input())
result = 0
k = 1
while N != 0:
    if k > N:
        k = 1
    N -= k
    k += 1
    result += 1

print(result)
    
  