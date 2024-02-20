# 이진 탐색
# 풀다가 막혀서 검색으로 힌트를 얻어 푼 문제다.
# 처음에 나무들의 높이에 꽂혀서 그걸로 이진탐색을 했다가 -> 모든 가능한 높이를 이진탐색 하도록 함
# 함수를 따로 만들어서 들고갈 수 있는 나무토막들의 길이를 계산하니 편했다.

N, M = map(int, input().split())
trees = sorted(list(map(int, input().split())))
max = trees[-1]  # 트리 중 최대 높이
possible = []

def calcWood(height):
    total = 0
    for i in range(0, len(trees)):
        if trees[i] > height:
            total += trees[i] - height
    return total


def binary_search(low, high, target):
    while low <= high:
        mid = (low + high) // 2
        tempM = calcWood(mid)
        if tempM == target:
            possible.append(mid)
            return mid
        if tempM > target:  # height를 더 크게
            low = mid + 1
            possible.append(mid)  # 나무토막들의 길이가 항상 M과 같을 수가 없다. 그래서 tempM이 M보다 클 때만 배열에 저장해야 한다
        if tempM < target:  # height를 더 낮게
            high = mid - 1
            # 여기서 tempM이 M보다 작은 상태에서 함수가 끝나도, 위의 경우가 최소 하나는 있기 때문에 괜찮다.
            # (가장 끝쪽 요소가 이진탐색의 끝자락에 저장된 것이므로 M과 가장 가까우면서 M보다 큰 값)


binary_search(0, max, M)
print(possible[-1])