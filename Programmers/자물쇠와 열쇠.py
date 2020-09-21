
def solution(key,lock):
    start = len(key)- 1 # expand list에서 lock의 시작 지점 
    end = start + len(lock) #expand list에서 lock의 끝 지점 
    expand_size = len(lock) + start * 2
    print(expand_size) # 7 
    for _ in range(4):
        for i in range(end):
            for j in range(end):
                if check(i,j,key,lock,expand_size,start,end):
                    return True
        key = spin(key)

    return False
                

# 4번 돌아야함 1. 그대로 2.90도 회전 3. 180도 회전 4. 270도 회전 
def spin(key):
    key_length = len(key)
    temp_key = [[0] * key_length for i in range(key_length)]
    reverse_i = key_length-1
    for i in range(key_length):
        for j in range(key_length):
            temp_key[j][reverse_i] = key[i][j]
        reverse_i -= 1
    
    return temp_key

def check(start_x,start_y,key,lock,expand_size,start,end):
     expand_list = [[0] * expand_size for _ in range(expand_size)] 
     for i in range(len(key)):
         for j in range(len(key)):
             expand_list[start_x+i][start_y+j] += key[i][j]
     
     for i in range(start,end): 
         for j in range(start,end):
             expand_list[i][j] += lock[i-start][j-start]
             if expand_list[i][j] != 1:
                 return False
     return True
    


 

if __name__ == "__main__":
    key = [[0,0,0],[1,0,0],[0,1,1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    solution(key,lock)
    


