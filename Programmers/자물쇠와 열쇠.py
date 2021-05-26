
import copy
def rotate(lst):
    listOfTuples = zip(*lst[::-1])
    return [list(elem) for elem in listOfTuples]

def chk(key,lock,x,y,m,n):
    temp = copy.deepcopy(lock)
    for i in range(x,x+m):
        if 0<=i<n:
            for j in range(y,y+m):
                if 0<=j<n:
                    temp[i][j] += key[i-x][j-y]
    for line in temp:
        for item in line:
            if item != 1:
                return False
    return True


def solution(key,lock):
    m = len(key)
    n  = len(lock)
    for _ in range(4):
        key = rotate(key)
        for i in range(-m+1,n):
            for j in range(-m+1,n):
                if chk(key,lock,i,j,m,n):
                    return True     
    return False

def printMatrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j],end=' ')
        print()
    print("-" * (len(mat[0]*2)))


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


print(solution(key, lock))