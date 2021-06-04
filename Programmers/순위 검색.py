def solution(info:list, query:list):
    answer = []

    candidates = []
    for inf in info:
        c = inf.split(' ')
        candidates.append([c[0],c[1],c[2],c[3],int(c[4])])

    querys = []
    for q in query:
        temp = []
        for qur in q.split(' '):
            if qur == "and":
                continue
            if qur.isdigit():
                qur = int(qur)
            temp.append(qur)
        querys.append(temp)
    
    query_length = 5
    for qur in querys:
        cnt = 0
        for cd in candidates:
            hit = 0
            for q,c in zip(qur,cd):
                if q == "-":
                    hit += 1
                    continue
                
                if type(c) == int:
                    if q <= c:
                        hit += 1
                else:
                    if q == c:
                        hit += 1
            if hit == query_length:
                cnt += 1
        answer.append(cnt)

    return answer

# 효율성 통과 x


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
solution(info,query)