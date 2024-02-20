# dfs
# dfs, bfs 예제코드 잘 되어있는 곳 : https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html

# 시간초과, 런타임 에러로 너무 힘들었던 문제
    # input을 sys.stdin.readline로 바꿔주었음
        # 런타임에러 안나게 하려면
            # 1. import sys 추가
            # 2. input 받고 반드시 .rstrip() 해주기
                # 입력이 많은 줄로 이루어져있을 때 훨씬 빠르게 입력받을 수 있습니다.
                # sys.stdin.readline은 input과 달리 개행 문자를 포함하여 반환합니다.
                # 따라서 split을 할 때 문제가 발생합니다. rstrip을 통해 끝의 개행 문자를 제거한 뒤에 수행해주어야 합니다.
    # select 리스트에 이미 방문한 노드를 표시할 때, stack 요소를 pop할 때 말고 stack에 append 할 때 표시해줘야 한다.
    # 영향이 큰지는 모르겠지만, 인접리스트 -> 인접행렬로 수정

# 인접리스트, 인접행렬의 시간복잡도
    # 상대적으로 인접리스트는 Node의 추가, 삭제가 빈번하게 발생하는 경우 사용하는 것이 좋습니다.
    # 상대적으로 인접행렬은 Edge의 추가, 삭제가 빈번하게 발생하는 경우 사용하는 것이 좋습니다.
    # https://wjjeong.tistory.com/38

import sys
sys.stdin = open('input.txt')

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
visited = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    visited[a][b] = visited[b][a] = 1

sk = deque()
selected = [0 for _ in range(N+1)]
result = 0
for n in range(1, N+1):
    if selected[n] == 0:
        sk.append(n)
        selected[n] = 1
        while sk:
            a = sk.pop()
            for i in range(1, N+1):
                if selected[i] == 0 and visited[a][i] == 1:
                    sk.append(i)
                    selected[i] = 1
        result += 1

print(result)


# 인접리스트 코드
# N, M = map(int, input().split())
# visited = [list() for _ in range(N+1)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     visited[a].append(b)
#     visited[b].append(a)
#
# sk = deque()
# selected = [0 for _ in range(N+1)]
# n = 1
# result = 0
# for n in range(1, N+1):
#     if selected[n] == 0:
#         sk.append(n)
#         while sk:
#             a = sk.pop()
#             selected[a] = 1
#             for i in visited[a]:
#                 if selected[i] == 0:
#                     sk.append(i)
#         result += 1
#
# print(result)
