def solution(clothes):
    ans={}
    
    for i in clothes:
        if i[1] in ans:
            ans[i[1]] += 1
        else:
            ans[i[1]] = 1
    cnt = 1
    for i in ans.values():
        cnt *= (i+1)
    return cnt -1 # 다 입지 않았을 때 수를 뺴줘야함



clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)