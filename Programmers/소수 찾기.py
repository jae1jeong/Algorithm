import itertools

def solution(numbers):
    all_numbers,ans = [],[]
    for i in range(1,len(numbers)+1):
        for perm in list(itertools.permutations(numbers,i)):
            perm = int("".join(perm))
            all_numbers.append(perm)
    max_prime = max(all_numbers)
    prime_list = get_prime(max_prime)
    for num in set(all_numbers):
        if num in prime_list:
            ans.append(num)
    return len(ans)

def get_prime(n):
    a = [False,False] + [True]*(n-1)
    primes=[]
    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False         
    return primes

print(solution("17"))
print(solution("011"))