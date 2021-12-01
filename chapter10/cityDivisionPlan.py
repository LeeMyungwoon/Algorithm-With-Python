# 도시 분할 계획
# 크루스칼 알고리즘 이용

# 루트노드 반환 매서드
def find_parent(parent, x):
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

# n = 노드, m = 간선
n, m = map(int, input().split())
parent = [0] * (n + 1)

# 부모노드 자기자신으로 초기화
for i in range(n + 1):
    parent[i] = i

edges = []   # 노드, 간선, 간선비용 담을 테이블 초기화

for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()   # 튜플이므로 첫번째 원소 기준으로 오름차순 정렬
result = 0

# find_parent 연산, union 연산 수행
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

# 결과출력
print(result - last)


