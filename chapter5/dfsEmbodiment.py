# dfs 구현
def dfs(graph, node, value):
    value[node] = True
    print(node, end = ' ')
    for a in graph[node]:
        if not value[a]:
            dfs(graph, a, value)
v, e = 8, 9
edges = [(1, 3), (3, 4), (3, 5), (4, 5), (1, 8), (1, 2), (2, 7), (7, 8), (7, 6)]
graph = [[]for _ in range(v + 1)]

# 그래프 연결리스트 구현
for s, e in edges:
    graph[e].append(s)
    graph[s].append(e)

# 그래프 연결리스트 오름차순 정렬
for i in range(v + 1):
    graph[i].sort()

value = [False] * 9
dfs(graph, 1, value)



