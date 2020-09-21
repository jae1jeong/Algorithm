import hashlib

str1 = str(input())

result = hashlib.sha256(str1.encode())
print(result.hexdigest())  # 해시 결과 문자열
