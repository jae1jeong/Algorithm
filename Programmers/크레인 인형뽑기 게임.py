


def solution(board,moves):
    bucket = []
    ans = 0
    idx = -1

    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                idx = board[i][move-1]
                board[i][move-1] = 0
                if len(bucket) > 0 and bucket[-1] == idx:
                    ans +=2
                    bucket.pop()
                else:
                    bucket.append(idx)
                break
    return ans
            
