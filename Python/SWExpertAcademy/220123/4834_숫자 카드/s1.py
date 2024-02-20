import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))

    # 카운트 배열 만들기 (인덱스: 숫자 종류, value: 숫자 개수)
    count = [0] * 10
    for i in cards:
        count[i] += 1

    result_count = -1  # 가장 많은 숫자 카드 개수
    result_val = -1  # 가장 많은 숫자 종류
    for i in range(9, -1, -1):  # 숫자가 큰 것을 우선으로 하니 뒤에서부터 순회
        if count[i] > result_count:  # 앞의 숫자는 뒤의 숫자보다 개수가 많아야 갱신된다
            result_count = count[i]
            result_val = i
    print('#{} {} {}'.format(tc, result_val, result_count))