
def solution(s):
    answer = []
    s = s[1:-1]
    nums= dict()
    temp = set()
    num = ""
    for string in s:
        if string == "{":
            temp = set()
        elif string == "}":
            if num.isdigit():
                temp.add(int(num))
                num = ""
            for t in temp:
                nums = addNumToDict(t,nums)
                    
        elif string == ",":
            if num.isdigit():
                temp.add(int(num))
                num = ""
        else:
            num += string
    else:
        if num.isdigit():
            addNumToDict(int(num),nums)

    for item in sorted(nums.items(),key= lambda x:x[1],reverse=True):
        answer.append(item[0])
    print(answer)
    return answer
        

def addNumToDict(number,numDict):
    if not number in numDict.keys():
        numDict[number] = 1
    else:
        numDict[number] += 1
    return numDict


solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")