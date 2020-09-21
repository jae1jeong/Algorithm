def solution(arr,divisor):
    #ans = [i for i in arr if i % divisor ==0 else i = -1]
    ans = []
    for i in range(0,len(arr)):
        if arr[i] % divisor ==0:
            ans.append(arr[i])
    if len(ans) == 0:
        ans.append(-1)
    else:
        ans = sorted(ans)
    return ans