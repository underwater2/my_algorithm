import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
rope = [int(sys.stdin.readline()) for _ in range(N)]
rope = sorted(rope, reverse=True)

weights = []
for i in range(1, N+1):
    weights.append(i * rope[i-1])

print(max(weights))