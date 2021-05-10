import sys
sys.stdin = open('input.txt','r')
word = input()
alphabet = [x for x in range(97,123)]

for x in alphabet:
    print(word.find(chr(x)))