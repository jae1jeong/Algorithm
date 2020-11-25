def solution(strings):
    start=0
    strings= list(strings)
    for idx in range(len(strings)):
        if strings[idx]==" ":start=0
        elif start == 0:
            if not str(strings[idx]).isdigit() and strings[idx].islower():
                strings[idx]=str(strings[idx]).upper()
            start +=1
        elif start>0:
            if strings[idx].isupper():
                strings[idx] = str(strings[idx]).lower()
            start +=1
    return "".join(strings)


def solution2(strings):
    return strings.title()

