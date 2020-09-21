import sys


def greedy(meeting):
    ctn = 0
    start_time = 0

    for time in meeting:
        if time[0] >= start_time:
            start_time = time[1]
            ctn +=1
    return ctn


a = int(sys.stdin.readline().strip())
meeting = []
for i in range(a):
    start,end = map(int,sys.stdin.readline().strip().split())
    meeting.append((start,end))
    # [(1,2),(2,3)]이런식으로 리스트 형식으로 저장

meeting = sorted(meeting, key=lambda  time : time[0])
meeting = sorted(meeting, key=lambda  time : time[1])
# end 기준으로 정렬
print(greedy(meeting))




