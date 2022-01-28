import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(range(1, 13))
    n = len(A)

    # 비트연산자로 부분집합 구하기
    # 모든 부분 집합을 만들어 답을 찾음. 실행 시간 : 0.16250s
    count = 0
    for i in range(1<<n):
        subset = []
        for j in range(n):
            if i & (1<<j):
                subset.append(A[j])
        if sum(subset) == K and len(subset) == N:
            count += 1
    print('#{} {}'.format(tc, count))


    # # (pass) 가지치기 해봤음. 실행 시간 : 0.15514s
    # count = 0
    # for i in range(1 << n):
    #     sub_len = 0
    #     sub_val = 0
    #     for j in range(n-1, -1, -1):  # 뒤에서부터 순회. 합이 큰 부분집합부터 가지치려고
    #         if i & (1 << j):
    #             sub_len += 1
    #             sub_val += A[j]
    #         if sub_len > N or sub_val > K:
    #             break
    #     if sub_len == N and sub_val == K:
    #         count += 1
    # print('#{} {}'.format(tc, count))





