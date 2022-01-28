# 공부한 내용 /for else문, /문자열 슬라이싱

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):

    # 문자열 슬라이싱해서 비교 가능한지 test
    # a = 'XYZ'
    # b = 'CDXYZDNKDG'
    #
    # if a == b[2:5]:
    #     print(True)

    str1 = input()
    len1 = len(str1)
    str2 = input()
    len2 = len(str2)
    cnt = 0

    for s in range(len2):  # 긴 문자열을 앞에서부터 하나씩 순화
        if str1 == str2[s: s+len1]:  # 문자열 슬라이싱 이용해서 서로 값이 일치하는지 보기
            cnt = 1
            break  # 일치하면 for문 끝내고 1 출력
    print('#{} {}'.format(tc, cnt))


    # 런타임 에러 난 코드 (왜인지 모르겠다)
    # 다른 사람들은 while문으로 많이 하고, if str2[s] != str1[0]: 로 걸러서 짰더라
    # for s in range(len2):
    #     if cnt != 0:
    #         break
    #     if str2[s] == str1[0]:
    #         for i in range(len1):
    #             if str2[s+i] == str1[i]:
    #                 if i == len1 -1:
    #                     cnt += 1
    #             else:
    #                 break
    # print('#{} {}'.format(tc, cnt))

