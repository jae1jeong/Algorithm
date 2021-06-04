from itertools import combinations

def solution(relation):
    answer = 0
    colSize = len(relation[0])
    rowSize = len(relation)
    candidates = []
    uniqueLst = []
    for i in range(1,colSize+1):
        candidates.extend(combinations(range(colSize),i))
    
    for candi in candidates:
        tmp = [tuple([item[i] for i in candi]) for item in relation]

        if len(set(tmp)) == rowSize:
            uniqueLst.append(candi)
    
    answer = set(uniqueLst)
    
    for i in range(len(uniqueLst)):
        for j in range(i+1,len(uniqueLst)):
            if len(uniqueLst[i]) == len(set(uniqueLst[i]) & set(uniqueLst[j])):
                answer.discard(uniqueLst[j])
    
    return len(answer)
        
        



relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
solution(relation)



