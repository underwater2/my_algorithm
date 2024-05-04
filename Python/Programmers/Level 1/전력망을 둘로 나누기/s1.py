from collections import deque

def solution(n, wires):
    adj = [[] for _ in range(n+1)]
    
    for wire in wires:
        adj[wire[0]].append(wire[1])
        adj[wire[1]].append(wire[0])
        
    answer = 1000
    for i in wires:
        adj[i[0]].remove(i[1])
        adj[i[1]].remove(i[0])
        # bfs
        count = 0
        q = deque()
        q.append(1)
        visited = [0] * (n+1)

        while q:
            now = q.popleft()
            count += 1
            visited[now] = 1

            for a in adj[now]:
                if not visited[a]:
                    q.append(a)
        answer = min(abs((n-count)-count), answer)
        # 원상복귀
        adj[i[0]].append(i[1])
        adj[i[1]].append(i[0])
        
    return answer
