

def match(n,string):
    repeat = 1
    temp = ""
    n = n+ 1
    while string[:n] == string[n-1:2*n] and n < len(string)-1:
        repeat += 1     
        temp = f'{repeat}{string[:n]}'
        n += n
        
    print(temp)
    

match(1,"aabbaccc")             