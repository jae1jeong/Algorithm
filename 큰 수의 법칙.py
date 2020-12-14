import sys
sys.stdin = open('input.txt','r')

n,m,k = map(int,input().split())
lst = sorted(list(map(int,input().split())),reverse=True)
ans = 0
cnt = 0 
# flag = True
# while flag:
#     for idx in range(len(lst)):
#         if cnt == m+1:
#             flag=False
#             break
#         ans += (k*lst[idx])
#         cnt += k
    
while cnt < m:
    if cnt+k <= m:
        ans += (lst[0] * k)
        cnt += k
    else:
        while cnt < m:
            ans += lst[0]
            cnt += k
    if cnt < m:
        ans += lst[1]
        cnt += 1
print(ans)
            



    