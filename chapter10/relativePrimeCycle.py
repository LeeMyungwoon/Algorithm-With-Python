# 서로소 집합을 활용한 사이클 판별

# 특정 원소가 속한 집합 판별
def find_parent(parent, x):
    # 원소와 부모노드가 같지 않다면
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

# 노드, 간선 입력
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 자기자신을 부모노드로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle == False:
    print("사이클 발생 안함")
else:
    print("사이클 발생")


