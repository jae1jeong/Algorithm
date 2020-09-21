dices = sorted(list(map(int, input().split())))


if len(set(dices)) == 1:
    print(10000+dices[0]*1000)
elif len(set(dices)) == 2:
    print(1000+dices[1]*100)
else:
    print(dices[2] * 100)
