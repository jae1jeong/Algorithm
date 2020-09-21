import copy

alphabet = {"A": 3, "B": 2, "C": 1, "D": 2, "E": 4, "F": 3, "G": 1, "H": 3, "I": 1, "J": 1,
            "K": 3, "L": 1, "M": 3, "N": 2, "O": 1, "P": 2, "Q": 2, "R": 2, "S": 1, "T": 2, "U": 1, "V": 1,
            "W": 1, "Y": 2, "Z": 1}

N, M = list(map(int, input().split()))
s1, s2 = input().split()


min_len = min(N, M)
union = []
for i in range(min_len):
    union += s1[i] + s2[i]

if N > M:
    union += s1[min_len:]
elif N < M:
    union += s2[min_len:]

lst = []
# for u in union:
#     lst.append(alphabet[u])
lst = [alphabet[i] for i in union]

while len(lst) > 2:
    temp = []
    for i in range(1, len(lst)):
        temp_num = lst[i] + lst[i-1]
        if temp_num >= 10:
            temp_num -= 10
        temp.append(temp_num)
    lst = copy.deepcopy(temp)

print("{}%".format(lst[0]*10 + lst[1]))
