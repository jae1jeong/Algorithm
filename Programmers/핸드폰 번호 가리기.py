
def solution(phone_number):
    phone_number = list(phone_number)
    for idx in range(0,len(phone_number)-4):
        phone_number[idx] = "*"
    return "".join(phone_number)

print(solution("01033334444"))
print(solution("027778888"))
