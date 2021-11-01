# bfs 구현

# 큐 구현을 위한 덱 임포트
from collections import deque

# bfs 매서드
def bfs(graph, num, visited):
    queue = deque([num])
    visited[num] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 연결리스트 그래프 구현
ver, edg = 8, 9
edges = [(1, 3), (3, 4), (3, 5), (4, 5), (1, 8), (1, 2), (2, 7), (7, 8), (7, 6)]
graph = [[]for _ in range(ver + 1)]
for f, l in edges:
    graph[f].append(l)
    graph[l].append(f)
for i in range(ver + 1):
    graph[i].sort()

visited = [False] * 9
bfs(graph, 1, visited)