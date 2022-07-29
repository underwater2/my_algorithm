from itertools import combinations

def solution(orders, course):
    answer = []
    # menus = dict()
    menulist = list()
    course.sort(reverse=True)
    for cnt in course:
        for order in orders:
            for comb in combinations(sorted(order), cnt):
                for prem in menulist:
                    if comb in prem:
                        break
                else:
                    menulist.append(comb)

    for prem in menulist:
        if menulist.count(prem) >= 2:
            answer.append(''.join(prem))

    # menu = ''.join(list(comb))
    # if menu in menus:
    #     menus[menu] += 1
    # else:
    #     menus[menu] = 1

    # for key in menus:
    #     if menus[key] >= 2:
    #         answer.append(key)
    return sorted(answer)