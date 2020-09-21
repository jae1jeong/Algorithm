

def dfs(n,lst,visit,result):

    if n == len(lst):
        print(result)

    else:
        for i in range(len(lst)):
            if not visit[i]:
                visit[i] = True
                result[n] = lst[i]
                dfs(n+1,lst,visit,result) 
                visit[i] = False

dfs(0,["a","b","c","d","e"],[0 for _ in range(5)],[0 for _ in range(5)])