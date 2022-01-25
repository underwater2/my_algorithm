# sort 함수 사용 안하고 정렬함

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    # 선택정렬
    for i in range(0, N-1):
        for j in range(i+1, N):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

    # 특별한 정렬 10개까지 구하기
    result = [0] * 10
    idx = 0
    for i in range(5):
        result[idx] = nums[N-1-i]
        idx += 1
        result[idx] = nums[i]
        idx += 1
    print('#{}'.format(tc), end=' ')
    print(*result)


    # # 선택정렬 더 빠르게 하기 (i 오른쪽의 요소중 가장 작은 것을 추리고 마지막에 i랑 자리 바꾸기)
    # for i in range(N-1):
    #     minIdx = i
    #     for j in range(i+1, N):
    #         if ai[minIdx] > ai[j]:
    #             minIdx = j
    #     ai[minIdx], ai[i] = ai[i], ai[minIdx]
