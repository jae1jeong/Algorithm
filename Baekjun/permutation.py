

def perm(arr,depth,n,k):
    
    if depth == k:
        print(arr)
        return
    
    for idx in range(depth,n):
        arr[idx],arr[depth] = arr[depth],arr[idx]
        perm(arr,depth+1,n,k)
        arr[idx],arr[depth] = arr[depth],arr[idx]


perm([1,2,3,4,5],2,,3)