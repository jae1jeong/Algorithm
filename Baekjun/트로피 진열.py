N = int(input())
trophy = []

def ascending(arr):
    now = arr[0]
    cnt = 1
    for i in range(1,len(arr)):
        if now < arr[i]:
            now = arr[i]
            cnt += 1
    return cnt

for _ in range(N):
    trophy.append(int(input()))

print(ascending(trophy))
trophy = trophy[::-1]
print(ascending(trophy))
