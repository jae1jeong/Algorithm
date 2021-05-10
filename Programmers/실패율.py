def solution(N, stages):
    answer = []
    leng = len(stages)
    fail_lst = []
    for i in range(1,N+1):
        count = stages.count(i)
        if leng == 0:
            fail = 0
        else:
            fail = count / leng
        
        leng -= count
        fail_lst.append((i,fail))

    fail_lst.sort(key= lambda x:-x[1])
    answer  = [x[0] for x in fail_lst]
    return answer


ss = [4,4,4,4,4]
n = 4

ss = [2, 1, 2, 6, 2, 4, 3, 3]
n = 5
solution(n,ss)