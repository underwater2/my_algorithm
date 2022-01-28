# # 딕셔너리 자료형 공부
# # https://wikidocs.net/16
# a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
# b = a.keys()
# print(list(b))
#
# # 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
# a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
# 'name' in a

# set 자료형 공부
# https://wikidocs.net/1015

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    # str1에 있는 글자들 찾기
    set1 = set()
    for s1 in str1:
        set1.add(s1)

    # str2에 몇 개씩 있는지 찾기
    dict2 = dict()
    for s2 in str2:
        if s2 in set1:
            if s2 in dict2:
                dict2[s2] += 1
            else:
                dict2[s2] = 1

    print('#{} {}'.format(tc, max(dict2.values())))