

N = int(input())


def dfs(n,current_row,current_candidate,final_result):# current_candidate 현재 퀸의 배치 정보 , final_result 답

    if current_row == n:
        final_result.append(current_candidate)
        return
    
    for candidate_col in range(n):
        if is_available(current_candidate,candidate_col):
            current_candidate.append(candidate_col)
            dfs(n,current_row+1,current_candidate,final_result)
            current_candidate.pop()



def solve(n):
    final_result = []
    dfs(n,0,[])

    return final_result
