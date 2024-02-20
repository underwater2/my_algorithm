def solution(s):
    nums = list(map(int, s.split()))
    minmax = [str(min(nums)), str(max(nums))]
    answer = ' '.join(minmax)
    return answer