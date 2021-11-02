# 미로탈출
# bfs 이용하여 문제 풀이

from collections import deque

# n -> 세로, m -> 가로 입력
n, m = map(int, input().split())

# 그래프 노드 입력
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우 방향벡터 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 0]

# bfs 매서드
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:   # 모든 노드를 탐색 했을 때 종료
        x, y = queue.popleft()   # 가장 아래 노드 접근
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵 범위를 벗어났을 때
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물을 만났을 때
            if graph[nx][ny] == 0:
                continue
            # 이동할 수 있을 때
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    return graph[n - 1][m - 1]

print(bfs(0, 0))   # 답안 출력력