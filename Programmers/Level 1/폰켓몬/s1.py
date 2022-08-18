from collections import Counter

def solution(nums):
    maxN = len(nums)//2
    num = Counter(nums)  # set()으로도 가능
    # min() 으로 대체해도 되는 부분
    if maxN <= len(num.keys()):  # len(num.keys()) == len(num)
        return maxN
    else:
        return len(num.keys())