def solution(clothes):
    ans=()
    
    answer = 0 +len(clothes)
    for i in range(len(clothes)):
        lst = (clothes[i])
        for j in range(len(clothes)):
            if i != j:
                if clothes[i][1] != clothes[j][1]:
                    lst.add(clothes[j])
                    
                    if lst not in ans:
                        ans.add(lst)
    print(ans)


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)