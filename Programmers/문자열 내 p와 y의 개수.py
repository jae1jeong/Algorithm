


def solution(String):

    s_map ={'p':0,'P':0,'y':0,'Y':0}

    for i in String:
        if not i in s_map:
            pass
        else:
            s_map[i] +=1

    if s_map['p'] + s_map['P'] == s_map['y'] + s_map['Y']:
        return True
    else:
        return False



'''
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')
    '''

