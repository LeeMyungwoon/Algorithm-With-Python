# 음료수 얼려먹기
# bfs 이용하여 문제풀이

from collections import deque

# n -> 세로, m -> 가로 입력
n, m = map(int, input().split())

# 그래프 노드 입력
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우 방향벡터 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    b = 1
    queue = deque()
    queue.append((x, y))

    # 칸막이일 경우
    if graph[x][y] == 1:
        a = 0
        return a   # 칸막이일 경우 0 반환

    while queue:
        x, y = queue.popleft()
        graph[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나는 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 이미 방문했거나, 칸막이일 경우
            if graph[nx][ny] == 1:
                continue

            # 방문 가능한 경우
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
    return b   # 방문가능했던 노드일 경우 1 반환

result = 0
for i in range(n):
    for j in range(m):
        result += bfs(i, j)
# 답안출력
print(result)
