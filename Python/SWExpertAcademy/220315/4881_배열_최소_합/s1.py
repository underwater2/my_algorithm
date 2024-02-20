# 시간초과나서 포기
# 0부터 N-1까지 숫자들의 순열을 구하고, 백트래킹으로 최솟값을 구한다
import sys
sys.stdin = open('sample_input.txt')

# 순열 구하기
# 1. 라이브러리 이용
# 반환값이 tuple
from itertools import permutations

# 2. 제너레이터(yelid)를 이용한 구현 - 한 원소를 뽑고 그 원소를 제외한 나머지 배열로 다시 함수 호출
# array: 문자열 또는 리스트, r: 만들려는 순열의 원소 개수
def permutations_2(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutations_2(array[:i] + array[i+1:], r-1):
                yield [array[i]] + next


def get_minV(perm):
    global minV
    total = 0
    idx = 0
    for i in perm:
        if minV < total:
            return
        else:
            total += arr[idx][i]
            idx += 1
    if minV > total:
        minV = total
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 987654321
    for i in permutations([i for i in range(0, N)], N):
        print(i, end=" ")
        get_minV(i)
    print('#{} {}'.format(tc, minV))

