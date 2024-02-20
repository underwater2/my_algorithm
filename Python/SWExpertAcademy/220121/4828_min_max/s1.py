# max, min 함수 쓰지 말라는 문제같아서 안썼다

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split())) # string으로 받고, 공백을 기준으로 숫자 분리, 하나씩 int 함수 적용해서 리스트에 넣기
    max_num = -1
    min_num = 987654321
    # 최댓값 구하기
    for i in nums:
        if max_num < i:
            max_num = i
        if min_num > i:
            min_num = i
    print('#{} {}'.format(tc, max_num - min_num))

