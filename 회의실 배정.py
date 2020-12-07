n= int(input())
meeting = []
for _ in range(n):
    start,end = map(int,input().split())
    meeting.append((start,end))
meeting.sort(key=lambda x: (x[1],x[0]))
et = 0
cnt = 0

for s,e in meeting:
    if et <= s:
        et = e
        cnt += 1
print(cnt)

        
        