import sys
import string
# sys.stdin = open('input.txt','r')


# P는 res인덱스용
def DFS(level,P):
    global cnt
    if level == code_length:
        cnt+=1
        for j in range(P):
            print(alpha_dict[res[j]],end=" ")
        print()
    
        
    else:
        for i in range(1,27):
            # 1자리
            if alpha_code[level] == i:
                res[P] = i
                DFS(level+1,P+1)

            elif i >= 10 and alpha_code[level] == i//10 and alpha_code[level+1] == i % 10:
                res[P] = i
                DFS(level+2,P+1)
                

if __name__ == '__main__':
    alpha_code = list(map(int,input()))
    code_length = len(alpha_code)
    alpha_code.append(-1) # 2자리 순회할때 마지막 인덱스가 오류나지 않게
    cnt = 0
    res = [0] * (code_length+3)
    alpha_dict = {
    }
    for idx,x in enumerate(string.ascii_uppercase,1):
        alpha_dict[idx]= x
    DFS(0,0)
    print(cnt)

    