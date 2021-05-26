from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    temp = set()
    menu_count = {}
    for cor in course:
        menu_count[cor] = defaultdict(int)
    for order in orders:
        for i in course:
            for x in combinations(order, i):
                menu = "".join(sorted(x))
                menu_count[i][menu] += 1

            
    for i in course:
        if len(menu_count[i]) == 0:
            continue
        max_value = max(menu_count[i].values())
        for menu in menu_count[i].keys():
            if menu_count[i][menu] >= 2 and menu_count[i][menu] == max_value:
                answer.append(menu)
    print(answer)            
    return sorted(answer)




solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])