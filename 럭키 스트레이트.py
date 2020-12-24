import sys
sys.stdin = open('input.txt','r')
lucky,ready = "LUCKY","READY"
score = str(input())
mid = len(score)//2
head,tail = score[:mid],score[mid:]
cnt1,cnt2 = 0,0
for h,t in zip(head,tail):
    cnt1 += int(h)
    cnt2 += int(t)
if cnt1 == cnt2:
    print(lucky)
else:
    print(ready)
