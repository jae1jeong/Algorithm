lst = list(str(input()) )
lst = [int(i) for i in lst]
lst = sorted(lst,reverse=True)
for i in lst: print(i,end="")


