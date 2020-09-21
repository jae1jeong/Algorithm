def solution(skill,skill_trees):
    st,ret = [],0
    for i in range(len(skill_trees)):
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in list(skill):               
                st.append(skill_trees[i][j])
        if chk(st,skill):
            ret += 1
        st = []
    return ret

def chk(skill_tree,skill):
    for idx in range(len(skill_tree)):
        if skill[idx] != skill_tree[idx]:
            return False
    return True
            

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))
            