N = int(input())
stack = list()
cnt = 1
ans = list()
flag = True

for i in range(1, N+1):
    data = int(input())
    while cnt <= data:
        stack.append(cnt)
        cnt += 1
        ans.append("+")
    if stack[-1] == data:
        stack.pop()
        ans.append("-")
    else:
        flag = False


if not flag:
    print("NO")
else:
    print("\n".join(ans))
