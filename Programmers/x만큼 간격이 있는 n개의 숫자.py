def solution(x,n):
    ans = 0
    lst = []
    for num in range(n):
        ans += x
        lst.append(ans)
    print(lst)
# solution(2,5)
# solution(4,3)
solution(-4,2)
