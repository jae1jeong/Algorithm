import sys
#sys.stdin = open('input.txt','r')
def DFS(level,idx):
    if level == L:
        ans.append(''.join(map(str,stk)))
        return
    else:
        for i in range(idx,C):
            stk.append(strings[i])
            DFS(level+1,i+1)
            stk.pop()            
def check_word(lst):
    for word in lst:
        cons = 0
        vol = 0
        for wd in word:
            if wd in "aeiou":
                cons += 1
            else:
                vol += 1
        
        if cons >= 1 and vol >= 2:
            print(word)
if __name__ == "__main__":
    L,C = map(int,input().split())
    strings = list(map(str,input().split()))
    strings.sort()
    stk = []
    ans = []
    DFS(0,0)
    check_word(ans)
