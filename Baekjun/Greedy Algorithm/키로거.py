
N = int(input())
anslist = []
for i in range(N):
    string = list(str(input()))
    idx = 0
    leftstack, rightstack = [], []
    for data in string:

        if data == "<":

            if leftstack:
                rightstack.append(leftstack.pop())

        elif data == ">":

            if rightstack:
                leftstack.append(rightstack.pop())

        elif data == "-":
            if leftstack:
                leftstack.pop()

        else:
            leftstack.append(data)

    leftstack.extend(reversed(rightstack))

    print("".join(leftstack))
