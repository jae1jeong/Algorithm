

def solution(record):
    answer = []
    user = {}
    
    board = []
    for rec in record:
        behave = rec.split()[0]
        user_id = rec.split()[1]
        if "Enter" == behave:
            user_name = rec.split()[2]
            user[user_id] = user_name
            board.append((user_id,"Enter"))
        
        elif "Leave" == behave:
            board.append((user_id,"Leave"))
        
        else:
            new_user_name = rec.split()[2]
            user[user_id] = new_user_name
    

    for chat in board:
        if chat[1] == "Enter":
            answer.append(f'{user[chat[0]]}님이 들어왔습니다.')
        else:
            answer.append(f'{user[chat[0]]}님이 나갔습니다.') 

    
    #print(answer)
    return answer



record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)