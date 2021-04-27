

def solution(people, limit):
    answer = 0
    people.sort()
    lt = 0
    rt = len(people) -1
    while lt < rt:
        if people[lt] + people[rt] <= limit:
            lt += 1
            rt -= 1
        else:
            rt -= 1
        answer += 1
    
    # 같다면 한명이 남아있으므로 보트 + 1
    if lt == rt:
        answer += 1
        
    return answer