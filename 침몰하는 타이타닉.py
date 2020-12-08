n,m = map(int,input().split())
peoples = list(map(int,input().split()))
peoples.sort()
# 정렬 후 몸무게가 가장 큰 사람과 작은 사람이 같이 탈 수 있는지 확인 후 안 되면 pop
cnt = 0

# 굳이 pop할 필요 없다. pop(0)하면 인덱스를 뒤에꺼를 한칸씩 떙겨야 되기 떄문에 시간복잡도 O(N) dequeue 쓰는게 좋을듯


while len(peoples) > 1:  
    if peoples[-1] + peoples[0] <= m:
        cnt += 1
        peoples.pop()
        peoples.pop(0)
    else:
        peoples.pop()
        cnt+= 1

if len(peoples) == 1:
    peoples.pop()
    cnt += 1

print(cnt)