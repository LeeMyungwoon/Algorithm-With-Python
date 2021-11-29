# 전보

import sys   # 많은 양의 데이터를 받아야 하므로 sys 라이브러리 임포트
import heapq   # 우선순위 힙 정렬 사용을 위해 heapq 라이브러리 임포트

INF = int(1e9)   # 무한대 표현을 위한 초기화
input = sys.stdin.readline   # 많은 양의 데이터 받아야 하므로 초기화

n, m, start = map(int, input().split())   # n -> 노드 개수, m -> 간선의 개수, start -> 시작노드

distance = [INF] * (n + 1)   # 거리 테이블 무한대 초기화
graph = [[] for _ in range(n + 1)]   # 그래프 테이블 초기화

# 그래프 노드, 간선, 간선비용 입력 및 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 다익스트라 우선순위 힙 정렬 매서드
def dijstra(start):
    q = []   # 큐 테이블
    distance[start] = 0   # 자기자신까지의 간선비용 0 초기화
    heapq.heappush(q, (0, start))   # 큐 +1
    while q:   # 큐의 원소가 없어질 때 까지
        dist, now = heapq.heappop(q)   # dist -> 간선비용, now -> 노드
        if dist > distance[now]:   # 현재 간선비용이 기존 간선비용보다 크면 무시
            continue
        for j in graph[now]:   # 현재 방문중인 노드
            cost = dist + j[1]   # cost = 방문중인 노드의 간선비용 + 기존노드의 간선비용
            if cost < distance[j[0]]:   # cost 값이 원래의 노드의 간선비용 보다 작으면 최신화
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))   # 큐 +1

dijstra(start)   # 다익스트라 매서그 실행

# 답안출력
add = 0
for i in range(2, n + 1):
    if distance[i] != INF:
        add += 1
print(add, end = ' ')

list = []
for i in range(n + 1):
    if distance[i] != INF:
        list.append(distance[i])
print(max(list))