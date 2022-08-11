# dfs 사용. bfs로 풀 수도 있다.

answer = 0

def dfs(arr, r, total, goal):
    global answer
    if r == len(arr):
        if total == goal:
            answer += 1
        return
    dfs(arr, r+1, total+arr[r], goal)
    dfs(arr, r+1, total-arr[r], goal)

def solution(numbers, target):
    dfs(numbers, 0, 0, target)
    return answer