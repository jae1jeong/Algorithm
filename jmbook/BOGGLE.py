
def hasWord(y,x,word):
    dx,dy = [-1,0,1,1,1,0,-1,-1],[1,1,1,0,-1,-1,-1,0]
    if (y > len(board)) and (x > len(board[0])): return False
    if word[0] != board[y][x]: return False
    if len(word) == 1: return True
    for idx in range(8):
        nx,ny = x+dx[idx],y+dy[idx]
        if hasWord(ny,nx,word[1:]):
            return True
    return False
test_case = int(input())


    
