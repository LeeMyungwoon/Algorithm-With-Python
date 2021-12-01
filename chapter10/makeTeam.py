# 팀 결성

# find_parent 같은팀 여부 확인
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union_parent 팀 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드, 간선개수 입력
n, m = map(int, input().split())
parent = [0] * (n + 1)

# 부모노드 자기자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

result = []   # 답안 문자열 저장 테이블

# 0, 1 판단후 결과 result 에 append
for i in range(m):
    conform, a, b = map(int, input().split())
    if conform == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            result.append("YES")
        else:
            result.append("NO")

# 결과출력
for i in result:
    print(i)

