def solution(strings, n):
    s = []
    for i in range(0,len(strings)):
        strings[i] = strings[i][n-1] + strings[i]
        
    strings = sorted(strings)
    print(strings)

    for i in range(len(strings)):
        s.append(strings[i][1:])

    print(s)
        
        




strings = ["sun","bed","car"]
solution(strings,1)

