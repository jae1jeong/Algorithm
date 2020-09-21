
N, S = input(), input()
S = list(S)
score, bonus = 0, 0

for idx, problem in enumerate(S, 1):
    if problem == "O":
        score += idx + bonus
        bonus += 1
    elif problem == "X":
        bonus = 0
print(score)
