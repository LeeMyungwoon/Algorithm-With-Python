# 개선된 서로소 집합 알고리즘 소스코드

# 루트노드 반환 매서드
def find_parent(parent, x):
    # 부모노드와 현재노드의 인자값이 같지 않을 때
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

# 각 노드의 부모노드를 자기자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 계산
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end = ' ')
for i in range(1, v + 1):
    print(find_parent(parent, i), end = ' ')

print(parent)