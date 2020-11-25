import os,sys

numbers = [i for i in range(1,6)]
input_txt = os.path.dirname(os.path.realpath(__file__)) + f'\in{}.txt'

async def read_txt(num):
    for i in range(1,6):
        input_txt = os.path.dirname(os.path.realpath(__file__)) + f'\in{i}.txt'
        f = open(input_txt,"r")
        line = f.readline()
        print(line)
    f.close()
# print(os.path.realpath(__file__))
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.realpath(__file__)))
