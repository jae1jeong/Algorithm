

# 빈번한 충돌을 개선하는 기법

# 해쉬 함수를 재정의 및 해쉬 테이블 저장공간을 확대

import hashlib
hash_table = list([0 for i in range(16)])


def hash_func(data):
    data % 16

# 파이썬 hash() 함수는 실행할 때마다, 값이 달라질 수 있음
# 유명한 해쉬 함수들이 있음: SHA(Secure Hash Algorithm) 어떤 데이터도 유일한 고정된 크기의 고정값을 리턴해주므로 해쉬 함수로 유용하게 활용 가능


# SHA-1
data = 'test1'.encode()  # 인코딩은 바이트로 바꿔준다 string은 유니코드
hash_object = hashlib.sha1()
hash_object.update(b'test')
hex_dig = hash_object.hexdigest()  # 16진수로 추출
print(hex_dig)  # a94a8fe5ccb19ba61c4c0873d391e987982fbbd3


# SHA-256
data = 'test1'.encode()  # 인코딩은 바이트로 바꿔준다 string은 유니코드
hash_object = hashlib.sha256()
hash_object.update(b'test')
hex_dig = hash_object.hexdigest()  # 16진수로 추출
print(hex_dig)  # a94a8fe5ccb19ba61c4c0873d391e987982fbbd3


def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16)


def hash_func(data):
    return data % 8


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_func(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[hash_address] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:  # 키가 동일하면 value를 업데이트
                hash_table[index][1] = value

    else:
        hash_table[hash_address] = [index_key, value]


def read_data(data):
    index_key = get_key(data)
    hash_adress = hash_func(index_key)

    if hash_table[hash_adress] != 0:
        for index in range(hash_adress, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None


print(get_key('db') % 8)
print(get_key('da') % 8)
print(get_key('dc') % 8)


# 시간 복잡도
# 일반적인 경우 O(1) 상당히 빠름
# 충돌이 있을 경우 O(N)