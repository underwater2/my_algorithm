def solution(n, words):
    w = set()
    w.add(words[0])
    for i in range(1, len(words)):
        w.add(words[i])
        if words[i-1][-1] != words[i][0] or len(w) != i+1:
            return [(i%n)+1, (i//n)+1]
    return [0,0]