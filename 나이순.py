N = int(input())
lst = list()

for _ in range(N):
    age,name = map(str,input().split())
    lst.append((int(age),name))

lst = sorted(lst,key=lambda x:x[0])
for i in lst:
    print('{} {}'.format(i[0],i[1]))



