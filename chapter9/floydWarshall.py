# 플로이드 워셜 알고리즘

INF = int(1e9)   # 무한대 표현을 위한 초기화

v = int(input())   # 노드입력
e = int(input())   # 간선입력
graph = [[INF] * (v + 1) for _ in range(v + 1)]   # 그래프 테이블 초기화

# 그래프 초기화
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 자신 노드비용 0으로 초기화
for i in range(1, v + 1):
    for j in range(1, v + 1):
        if i == j:
            graph[i][j] = 0

# 간선비용이 가장 작은 것으로 그래프 간선비용 초기화
for i in range(1, v + 1):
    for j in range(1, v + 1):
        for k in range(1, v + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 결과출력
for i in range(1, v + 1):
    for j in range(1, v + 1):
        if graph[i][j] == INF:
            print("INFINITY", end =' ')
        else:
            print(graph[i][j], end = ' ')
    print()