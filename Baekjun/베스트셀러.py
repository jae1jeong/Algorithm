N = int(input())
data = {}
key_list = []

for i in range(N):
    book = input()
    if book not in data:
        data[book] = 1
    else:
        data[book] += 1

target = max(data.values())
arr = []

for book,number in data.items():
    if number == target:
        arr.append(book)



print(sorted(arr)[0])

