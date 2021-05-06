import sys
sys.stdin = open('input.txt','r')
chk = [-1] * 25
string = input()
for i in range(len(string)):
    if 0<=(ord(string[i])-97)<26:
        if chk[ord(string[i])-97] == -1:
            chk[ord(string[i])-97] = i
    else:
        print(-1)
        sys.exit()
for j in range(25):
    print(str(chk[j]),end=" ")