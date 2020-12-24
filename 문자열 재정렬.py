import sys
sys.stdin = open('input.txt','r')
string = str(input())
alph,nums = "",0
for st in string:
    if st.isalpha():
        alph += st
    else:
        nums += int(st)
alph= sorted(alph)
nums = str(nums)
alph += nums
print("".join(alph))