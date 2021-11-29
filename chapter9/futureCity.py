# 미래도시

INF = int(1e9)   # 무한대 표현을 위한 초기화

# n -> 노드의 개수, m -> 간선의 개수
n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]   # 그래프 테이블 (n + 1)크기만큼 초기화

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1   # 간선비용이 1이므로 1로 초기화
    graph[b][a] = 1   # 노드끼리 양뱡향 연결 리스트 이므로 반대 노드끼리도 1로 초기화

x, k = map(int, input().split())   # x, k 입력

# 자기자신으로의 간선비용 0 초기화 매서드
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 플로이드 워셜 알고리즘 매서드
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = graph[1][k] + graph[k][x]   # 1에서 k까지, k에서 x까지 거리의 합

# 결과출력
if result >= INF:
    print(-1)
else:
    print(result)