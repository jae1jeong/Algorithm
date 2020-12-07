def solution(citations):
    answer = 0
    citations = sorted(citations)
    def chk(num):
        cnt = 0
        for i in range(len(citations)):
            if citations[i] >= num:
                cnt += 1
        return cnt
    for i in range(len(citations)-1):
        if citations[i+1] > citations[i] and chk(citations[i+1]) < chk(citations[i]):
            answer = chk(citations[i])
            break
    print(answer)
        
        
num    0 1 3 5 6
chk(i) 5 4 3 2 1 


    

citations = [3,0,6,1,5]
solution(citations)