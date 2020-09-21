
lst = [int(input()) for i in range(9)]  # 크기가 9인 리스트를 입력 받는다.
ans = []
lst.sort()  # 답이 정렬되어 있기 때문에 미리 정렬한다.
for i in range(len(lst)):
    for j in range(1, len(lst)):

        # 난쟁이들의 합 - (반복문을 돌면서 모든 요소들을 두 개)이 100이라면 난쟁이들이 아니다.
        if sum(lst) - (lst[i] + lst[j]) == 100:
            ans.append(lst[i])
            ans.append(lst[j])

lst.remove(ans[0])  # 난쟁이들이 아닌 것을 삭제
lst.remove(ans[1])


for i in lst:
    print(i)
