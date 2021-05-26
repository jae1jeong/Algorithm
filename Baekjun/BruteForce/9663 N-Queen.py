import sys
sys.stdin = open('input.txt','r')


def chk(candidate_lst,current_col):
    current_row = len(candidate_lst)

    for queen_row in range(current_row):
        if candidate_lst[queen_row] == current_col or abs(candidate_lst[queen_row] - current_col) == current_row - queen_row:
            return False
    return True

def DFS(x,y,candidateLst):
    global cnt

    if x == n:
        cnt += 1
        return

    for i in range(n):
        if len(candidateLst) > 0 and candidateLst[x-1] == i:
            continue

        if chk(candidateLst, i):
            candidateLst.append(i)
            DFS(x+1,i,candidateLst)
            candidateLst.pop()

if __name__ == "__main__":
    n = int(input())
    queenLst = []
    cnt = 0
    DFS(0,0,[])
    print(cnt)

