k,n = map(int,input().split())
line = []
res = 0
largest = 0
for _ in range(k):
    temp = int(input())
    line.append(temp)
    largest = max(largest,temp)

def chk(num):
    cnt = 0
    for x in line:
        cnt += (x//num)
    return cnt

lt,rt = 0,largest
while lt <= rt:
    mid = (lt+rt)//2
    lan_chk = chk(mid) 
    if lan_chk >= n:
        res = mid
        lt = mid +1
    else:
        rt = mid -1
print(res)
    
    