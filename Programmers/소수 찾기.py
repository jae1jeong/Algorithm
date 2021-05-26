def solution(numbers):
    cnt = 0
    tupleNums = set()
    _max = -1
    def DFS(level,length,chk,res):
        nonlocal _max
        if level == length:
            temp = ''
            for j in range(length):
                temp += res[j]  
            _max = max(int(temp),_max)          
            tupleNums.add(int(temp))

        else:
            for i in range(len(numbers)):
                if not chk[i]:
                    chk[i] = True
                    res[level] = numbers[i]
                    DFS(level+1,length,chk,res)
                    chk[i] = False

    for i in range(1,len(numbers)+1):
        chk = [False] * (len(numbers)+1)
        res = [0] * (len(numbers)+1)
        DFS(0,i,chk,res)
    
    primeLst = getPrime(_max)
    for num in tupleNums:
        if primeLst[num]:
            cnt += 1

    return cnt 

def getPrime(numbers:int)->list:
    chk = [False,False] + [True] * (numbers-1)
    for i in range(2,numbers+1):
        if chk[i]:
            for j in range(2*i,numbers+1,i):
                chk[j] = False
    return chk

print(solution("17"))