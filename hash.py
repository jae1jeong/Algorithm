
# hashtable 미리 생성 0으로 초기화
hash_table = [0 for _ in range(10)]


def hash_func(key):
    return key % 5


def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value


def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]


storage_data('Andy', '01073023600')
storage_data('Babe', '01099999999')

# hash 내장함수

hash_table = [0 for _ in range(10)]


def get_key(data):
    #print(f' data is {data} hash is {hash(data)}')
    return hash(data)


def hash_function(key):
    #print(f'key is {key}')
    return key % 8


def save_data(data, value):
    #hash_address = hash_function(get_key(data))
    print(f' data is {data} hash address is {hash_address}')
    hash_table[hash_address] = value


def read_data(data):
    #hash_address = hash_function(get_key(data))
    return hash_table[hash_address]


#save_data('Dave', '01031231234')
#save_data('David', '01031236666')


# print(read_data('Dave'))
