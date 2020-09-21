
def dfs_perm(lst,n):
    
    ret = []
    idx = [i for i in range(len(lst))] #[0,1,2,3,4]

    stack = []
    
    for i in idx:
        stack.append([i])

    while len(stack) != 0:
        cur = stack.pop()
        for i in idx:
            if i not in cur:
                temp = cur+[i]

                if len(temp) == n: 
                    element = []
                    for i in temp:
                        element.append(lst[i])
                    ret.append(element)
                else:
                    stack.append(temp)
    return ret
 
print(dfs_perm([7,1],2)) 