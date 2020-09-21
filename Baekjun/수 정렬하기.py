N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))


def quick_sort(lst:list):
    
    if len(lst) <= 1:
        return lst
    
    pivot = lst[0]
    lst = lst[1:]
    left = [i for i in lst if pivot > i]
    right = [i for i in lst if pivot <= i]
    
    return quick_sort(left) + [pivot] + quick_sort(right)


for i in lst:
    print(i)


