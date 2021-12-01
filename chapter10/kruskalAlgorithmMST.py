# 크루스칼 알고리즘 최소신장 트리

# 루트노드 반환 매서드
def find_parent(parent, x):
    # 부모노드와 인자값이 다를 때
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 매서드
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드, 간선의 개수 입력
v, e = map(int, input().split())
parent = [0] * (v + 1)
edges = []
result = 0

# 초기 자기자긴을 부모노드로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선정보 입력
for i in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()   # 간선비용 기준 오름차순 정렬

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):   # 두개의 루트노드가 같지 않을때 -> 사이클이 발생하지 않을 때
        union_parent(parent, a, b)   # 힙치기 연산
        result += cost

# 결과출력
print(result)