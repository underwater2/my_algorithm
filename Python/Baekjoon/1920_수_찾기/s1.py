# 이진 탐색

def binarySearch(ai, low, high, target):
    while low <= high:
        mid = (low + high) // 2
        if target > ai[mid]:
            low = mid + 1
        if target < ai[mid]:
            high = mid - 1
        if target == ai[mid]:
            result.append(1)
            break
        if low > high:
            result.append(0)


N = int(input())
ai = sorted(list(map(int, input().split())))
M = int(input())
bi = list(map(int, input().split()))

result = []

for target in bi:
    binarySearch(ai, 0, N-1, target)

for i in range(0, len(result)):
    print(result[i])