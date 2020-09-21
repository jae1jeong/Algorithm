import itertools
N,S = map(int,input().split())
lst = list(map(int,input().split()))
cnt = 0
for i in range(1,N+1):
    for j in list(itertools.combinations(lst,i)):
        if sum(j) == S:
            cnt += 1
print(cnt)
    