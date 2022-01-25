import sys
sys.stdin = open('sample_input.txt')

# 재귀는 시간초과날 것 같아서 while문으로 구현
def binary_search(page, goal):
    left = 1
    right = page
    cnt = 0
    while 1:  # 반드시 goal을 찾으니 무한반복 해도 됨
        middle = (left + right) // 2
        cnt += 1
        if goal < middle:  # 찾으려는 페이지가 편 곳보다 왼쪽
            right = middle  # 이렇게 해도 답은 나오는데, right = middle - 1이 맞는듯
        elif goal > middle:  # 찾으려는 페이지가 편 곳보다 오른쪽
            left = middle  # 이렇게 해도 답은 나오는데, left = middle + 1이 맞는듯
        elif goal == middle:
            break  # 찾았으면 while문 탈출
    return cnt


T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    result = binary_search(P, Pa) - binary_search(P, Pb)
    if result == 0:
        print('#{} {}'.format(tc, 0))
    elif result < 0:
        print('#{} {}'.format(tc, 'A'))
    elif result > 0:
        print('#{} {}'.format(tc, 'B'))


    # print(binary_search(P, Pa))
    # print(binary_search(P, Pb))