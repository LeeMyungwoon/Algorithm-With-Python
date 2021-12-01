# 위상정렬

from collections import deque   # 큐 자료구조 이용을 위한 덱 라이브러리 import

v, e = map(int, input().split())   # 노드, 간선정보 입력
indegree = [0] * (v + 1)   # 진입차수 테이블 초기화
graph = [[] for _ in range(v + 1)]   # graph 테이블 초기화

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

    indegree[b] += 1   # 들어가는 노드이기 때문에 해당 노드의 진입차수 +1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:   # 진입차수가 0이면 큐에 넣는다
            q.append(i)
            break   # 초기 이므로 진입차수 0 발견하면 바로 탈출

    while q:
        now = q.popleft()   # 큐에서 하나 pop
        result.append(now)

        for i in graph[now]:   # 이전노드에서 들어오는 간선 제거하므로 해당노드의 진입차수 -1
            indegree[i] -= 1
            if indegree[i] == 0:   # 연결되어 있는 다음 노드의 진입차수가 0이면 다시 큐에 append
                q.append(i)

    # 결과 출력
    for i in result:
        print(i, end = ' ')

topology_sort()

