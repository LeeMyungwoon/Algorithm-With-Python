# 음료수 얼려먹기
# dfs 이용하여 문제풀이

# 가로, 세로 입력받기
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# dfs 매서드
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 빈 공간이면 상, 하, 좌, 우 재귀함수 탐색
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

result = 0   # 방문하는 횟수
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
# 결과출력
print(result)