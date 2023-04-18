def solution(skill, skill_trees):
    skillIdx = dict()
    for i in range(len(skill)):
        skillIdx[skill[i]] = i
    print(skillIdx)
    
    answer = 0
    for skill_tree in skill_trees:
        num = 0
        for s in skill_tree:
            if s in list(skill):
                if skillIdx[s] != num:
                    break
                else:
                    num += 1
        else:
            answer += 1
    return answer