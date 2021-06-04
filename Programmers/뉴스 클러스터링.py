from collections import defaultdict

def solution(str1:str, str2:str):
    answer = 0
    strDict1 = defaultdict(int)
    strDict2 = defaultdict(int)

    lst1,lst2 = onlyAlphabet(str1),onlyAlphabet(str2)
    countDict(lst1,strDict1)
    countDict(lst2,strDict2)

    interaction = []
    for string in lst1:
        if string in lst2:
            interaction.append(string)
    union = []
    jacardo = [x for x in lst1] + [x for x in lst2]
    print(jacardo)
    

    
    

def countDict(lst:list,dictionary:defaultdict):
    for string in lst:
        dictionary[string] += 1
    return dictionary
        


def onlyAlphabet(string:str):
    
    temp= []
    for i in range(len(string)-1):
        if string[i].isalpha() and string[i+1].isalpha():
            temp.append((string[i]+string[i+1]).upper())
    
    return temp

    
solution("aa1+aa2","AAAA12")