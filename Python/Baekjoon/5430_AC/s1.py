# 문자열
# list 다루는 것도 중요한 문제
# if p[i+1] == 'R':  에서 인덱스 에러가 나는 걸 몰라서 틀렸다가,
# reverse()를 최적화해봤더니 시간초과 나지 않고 맞았다.


import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    p = input()
    n = int(input())
    nums = input()
    if nums != '[]':
        nums = deque(map(int, nums[1:len(nums)-1].split(',')))
    else:  # 배열이 []일 때
        nums = deque()


    try:
        i = 0
        status = True  # True일 때 원래 순서, False일 때 반대 순서
        while i < len(p):
            if p[i] == 'D':
                if status:
                    nums.popleft()
                elif not status:
                    nums.pop()
                i += 1
            else:
                if i == len(p) - 1:
                    status = not status
                    i += 1
                    break

                if p[i+1] == 'R':
                    i += 2
                else:
                    status = not status
                    i += 1
        if not status:
            nums.reverse()

        print('[', end='')
        print(*list(nums), sep=',', end='')
        print(']')
    except:
        print('error')


    # (시간초과) reverse 최적화하기 전
    # try:
    #     i = 0
    #     while i < len(p):
    #         if p[i] == 'D':
    #             nums.popleft()
    #             i += 1
    #         else:
    #             if i == len(p) - 1:
    #                 nums.reverse()
    #                 i += 1
    #                 break
    #
    #             if p[i+1] == 'R':
    #                 i += 2
    #             else:
    #                 nums.reverse()
    #                 i += 1
    #     print('[', end='')
    #     print(*list(nums), sep=',', end='')
    #     print(']')
    # except:
    #     print('error')


# 빈칸 없이 list 출력하기
# li = [1, 2, 3, 4]
# print(*li, sep=',')

# list reverse 하기
# lis = [2, 4, 1, -1]
# print(list(reversed(lis)))
