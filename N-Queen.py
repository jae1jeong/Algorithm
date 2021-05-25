

import sys
sys.stdin = open('input.txt','r')


def DFS(n,current_row,current_candidate,final_result):
    if current_row == n:
        final_result.append(current_candidate[:])

    for candidate_col in range(n):
        if check(current_candidate,candidate_col):
            current_candidate.append(candidate_col)
            DFS(n,current_row+1,current_candidate,final_result)
            current_candidate.pop()

def check(candidate,current_col):
    current_row = len(candidate)

    for queen_row in range(current_row):
        if candidate[queen_row] == current_row or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True

if __name__ == "__main__":
    
    n = int(input())
