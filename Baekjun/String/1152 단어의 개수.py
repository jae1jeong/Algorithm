import sys
sys.stdin = open('input.txt','r')
string_lst = input().strip().split(" ")

if len(string_lst) == 1 and string_lst[0]== '':
    print(0)
else:
    print(len(string_lst))