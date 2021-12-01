# 서로소 집합 알고르즘 기본

# 루트노드 반납 매서드
def find_parent(parent, x):
    # 확인중인노드와 부모노드가 같지 않을 때
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

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

# 자기자신으로 부모노드 초기화
for i in range(v + 1):
    parent[i] = i

# union 연산 입력
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end = ' ')
for i in range(1, v + 1):
    print(find_parent(parent, i), end = ' ')
print()

# 각각노드의 부모테이블 출력
print("부모 테이블: ", end = ' ')
for i in range(1, v + 1):
    print(parent[i], end = ' ')

