n = int(input())
players = []
for _ in range(n):
    tall,weight = map(int,input().split())
    players.append((tall,weight))

players.sort(reverse=True)
largest=  0
cnt = 0
for x,y in players:
    if largest < y:
        cnt += 1
        largest = y
print(cnt)