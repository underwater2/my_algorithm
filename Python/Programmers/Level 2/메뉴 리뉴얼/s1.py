# 문제를 이해하기 어려웠다
    # 각 메뉴구성 개수 마다 빈도가 가장 많은 조합만 return

from itertools import combinations

def solution(orders, course):
    answer = []
    menus = dict()
    course.sort(reverse=True)
    for cnt in course:
        for order in orders:
            for comb in combinations(sorted(order), cnt):
                menu = ''.join(list(comb))
                if menu in menus:
                    menus[menu] += 1
                else:
                    menus[menu] = 1

    sorted_menus = sorted(menus.items(), key = lambda item: item[1], reverse = True)
    print(sorted_menus)
    maxN = [0] * 11
    for menu in sorted_menus:
        if not course or menu[1] < 2:
            break
        elif len(menu[0]) in course:
            maxN[len(menu[0])] = menu[1]
            course.remove(len(menu[0]))
        else:
            continue
    print(maxN)

    for n in range(2, 11):
        if maxN[n]:
            for menu in sorted_menus:
                if len(menu[0]) == n and menu[1] == maxN[n]:
                    answer.append(menu[0])

    return sorted(set(answer))