def solution(elements):
    nums = set(elements)
    nums.add(sum(elements))
    for i in range(len((elements))):
        n = elements[i]
        for j in range(1, len(elements)-1):
            idx = (i+j) % len(elements)
            n += elements[idx]
            nums.add(n)
    return len(nums)