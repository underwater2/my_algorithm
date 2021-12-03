# 샘플값에 맞게 출력 잘 나오는데 계속 틀리다고 뜸
# 인터넷에서 긁어온 자바코드 제출해도 안됨
# 이 문제 버리기로

import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    Q = int(input())
    bi = list(map(int, input().split()))

    result = []

    # 이진탐색
    for target in bi:
        low = 0
        high = len(ai)-1
        while low <= high:
            mid = (low + high) // 2
            if target > ai[mid]:
                low = mid + 1
            if target < ai[mid]:
                high = mid - 1
            if target == ai[mid]:
                result.append(mid)
                break
            if low > high:
                result.append(-1)
    print(*result)