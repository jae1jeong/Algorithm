from itertools import permutations

def solution(users_id,banned_id):
    ans = []
    for perm_users in permutations(users_id,len(banned_id)): # user 아이디들의 모든 경우들을 체크한다.
        if chk(perm_users,banned_id):
            perm_users = set(perm_users)
            print(perm_users)
            if perm_users not in ans: # 중복되는 케이스 제거
                ans.append(perm_users)
    return len(ans)
        
# 아이디 길이 체크
def chk(users_id,banned_id):
    for i in range(len(banned_id)):
        if len(users_id[i]) != len(banned_id[i]): 
            return False
        if not is_match(users_id[i],banned_id[i]): 
            return False
    return True
        

# *는 넘기고 아이디 문자가 같은지 체크
def is_match(user_id,ban_id):
    for i in range(len(ban_id)):
        if ban_id[i] == "*":
            continue
        elif user_id[i] != ban_id[i]:
            return False
    return True


# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"])
# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])
