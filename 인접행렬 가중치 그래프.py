import sys



# 한 번 방문한 노드는 방문하지 않는다. 계속 방문하게 되면 함수가 안 끝남      
# sys.stdin = open('input.txt','r')
n,m = map(int,input().split())
cnt = 0
chk_lst = [0] * (n+1)
matrix = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    index,num = map(int,input().split())
    matrix[index][num] = 1


def dfs(vertex):
    global cnt
    
    if(vertex == n):
        cnt += 1
        return

    else:
        for i in range(1,n+1):
            if chk_lst[i] == 0 and matrix[vertex][i] == 1:
                chk_lst[i] = 1
                dfs(i)
                chk_lst[i] = 0 

chk_lst[1] = 1
dfs(1)
print(cnt)