

import itertools

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]

members= [i for i in range(N)]

teams1= list(itertools.combinations(members,N//2))
ans = 1e9
people = list(range(N))
for group in teams1:
    rest = list(set(people) - set(group))
    group_sum,rest_sum = 0,0
    group_comb = list(itertools.combinations(group,2))
    rest_comb = list(itertools.combinations(rest,2))

    for g,r in zip(group_comb,rest_comb):
        x1,y1 = g
        group_sum += matrix[x1][y1]+  matrix[y1][x1]
        x2,y2 = r
        rest_sum  += matrix[x2][y2] + matrix[y2][x2]

    ans = min(ans,abs(group_sum-rest_sum))

print(ans)
    