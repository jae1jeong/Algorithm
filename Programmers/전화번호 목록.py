
def solution(phone_book):  
    
    for phone1 in phone_book:
        for phone2 in phone_book:
            if phone1 == phone2 or len(phone1) > len(phone2): continue
            idx = len(phone1)
            if phone1[:idx] == phone2[:idx]:
                return False
    return True


