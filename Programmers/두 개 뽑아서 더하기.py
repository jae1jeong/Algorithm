def solution(numbers):
    ans = set()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j: continue
            ans.add(numbers[i]+numbers[j])
    return sorted(list(ans))
        

