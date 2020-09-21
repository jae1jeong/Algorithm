hash_table = [0 for _ in range(8)]
# 저장공간 활용도를 높일 수 있다.


def get_key(data):
    return hash(data)


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


print(hash('dk') % 8)
print(hash('da') % 8)
save_data('dk', '010123123123')
save_data('da', '333333333333')
print(read_data('dk'))
