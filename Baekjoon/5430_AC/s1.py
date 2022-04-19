import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    p = input()
    n = int(input())
    nums = input()
    if nums != '[]':
        nums = list(map(int, nums[1:len(nums)-1].split(',')))
    else:  # 배열이 []일 때
        continue

# li = [1, 2, 3, 4]
# print(*li, sep=',')

# lis = [2, 4, 1, -1]
# print(list(reversed(lis)))
