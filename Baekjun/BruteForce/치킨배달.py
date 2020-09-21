import itertools
import math


def distance(house,shop):
    res = 0 

    for h in house:
        tmp_min = math.inf
        hx,hy = h 
        for s in shop:
            sx,sy = s
            if tmp_min > abs(hx-sx)+abs(hy-sy):
                tmp_min = min(tmp_min,abs(hx-sx)+abs(hy-sy))
        res += tmp_min
    return res




n,m = map(int,input().split())
house,shop,pick = [],[],[]
matrix = [list(map(int,input().split())) for _ in range(n)]

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == 1:
            house.append([i,j])
        elif matrix[i][j] == 2:
            shop.append([i,j])


min_res = math.inf
for i in list(itertools.combinations(shop,m)):
    result = distance(house,i)
    if result < min_res:
        min_res = result

print(min_res)

