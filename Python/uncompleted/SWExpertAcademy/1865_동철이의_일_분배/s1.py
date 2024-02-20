# 순열 (중복 x)
# 10!, 11!, 12!가 대략 1초 정도 걸린다.
# 1 <= N <= 16 이니 시간이 오래 걸릴 것 => 가지치기를 해야한다.

# 그리디는 최선도, 최악도 보장할 수는 없다.
# 여기서는 그리디로 ans의 로컬값을 하나 구해놓은 후에 가지치기를 한다. => 검색 노드수가 줄었다. 더 많은 가지치기를 할 수 있다.

# 쓰다 말음
# import sys
# sys.stdin = open('input.txt', 'r')
#
# def solve(k, val):  # k는 depth (몇 개 선택했는지)
#     global ans
#     global cnt
#     cnt += 1
#     if k == N:
#         if val > ans:
#             ans = val
#     else:
#         for i in range(k, N):
#             perm[k], perm[i] = perm[i], perm[k]
#             if val * mat[k][perm[k]] > ans:
#                 solve(k+1, val * mat[k][perm[k]])
#             perm[i], perm[k] = perm[k], perm[i]
#
#
# TC = int(input())
# for tc in range(1, TC+1):
#     N = int(input())
#
#     # 2차원배열을 받았다.
#     mat = [0.0] * N
#     for i in range(N):
#         mat[i] = list(map(lambda x: int(x)/100, input().split()))
#
#     cnt = 0
#     ans = 0
#     perm = [x for x in range(N)]  # 순열을 저장하는 배열
#     solve(0)
#     print("#%d %.6f" % (tc, ans * 100))
#


# 답 이상함...
# 순열 계산 방식이 N! 이라서 12 넘어가면 너무 오랜 시간이 걸린다. => 코드 바꿔야함
import sys
sys.stdin = open('input.txt', 'r')

def solve(k):  # k는 depth (몇 개 선택했는지)
    global ans
    if k == N:
        val = 1
        for i in range(N):
            val *= mat[i][perm[i]]
        if val > ans:
            ans = val
    else:
        for i in range(k, N):
            perm[k], perm[i] = perm[i], perm[k]
            solve(k+1)
            perm[k], perm[i] = perm[i], perm[k]


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 2차원배열을 받았다.
    mat = [0.0] * N
    for i in range(N):
        mat[i] = list(map(lambda x: int(x)/100, input().split()))

    ans = 0
    perm = [x for x in range(N)]  # 순열을 저장하는 배열
    solve(0)
    print("#%d %.6f" % (tc, ans * 100))