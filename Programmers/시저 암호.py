def solution(strings,n):
    temp=[]
    for string in strings:
        if string == " ":
            temp.append(string)
        elif string.isalpha():
            if string in ["z","Z"]:
                
            # if string.isupper():
            #     if ord(string) > 90:
            #         string = chr(ord(string)-26+n)
            #     else:
            #         string = chr(ord(string)+n)
            # elif string.islower():
            #     if ord(string)> 120:
            #         string = chr(ord(string)-26+n)
            #     else:
            #         string = chr(ord(string)+n)
            temp.append(string)
    return "".join(temp)



solution("a B z",4)