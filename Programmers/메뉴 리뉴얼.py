from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    temp = set()
    menu_count = defaultdict(int)
    for order in orders:
        for i in range(2,len(order)+1):
            for x in combinations(list(order),i):
                for j in range(len(orders)):
                    menus = set(orders[j])
                    if len(x)>len(menus):
                        continue
                    intersectionMenu = menus.intersection(sorted(x))
                    if len(intersectionMenu) >= 2:
                        menu_count[''.join(sorted(intersectionMenu))] += 1
    
            print(menu_count)
            menu_count = defaultdict(int)

    
    return answer




solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])