n,c = map(int,input().split())
Line = []
for _ in range(n):
    Line.append(int(input()))
Line.sort()
lt = 1
rt = Line[-1]

def Count(dis):
    cnt = 1
    ep = Line[0]
    # 첫번째 구간은 말 배치했으니까 1부터
    for i in range(1,len(Line)):
        if Line[i] - ep >= dis:
            cnt += 1 # 말 배치
            ep = Line[i]
    return cnt


while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)