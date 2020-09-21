
def hanoi(num,start,to,via):
    if num == 1:
        return
    
    hanoi(num-1,start,via,to)

    hanoi(num-1,start,to,via)