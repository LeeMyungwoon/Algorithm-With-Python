# 우선순위 힙 자료구조 이용한 다익스트라 최단경로 알고리즘

import sys   # 많은양의 데이터 입력받기 위한 임포트
import heapq   # 우선순의 힙 구현을 위한 임포트

input = sys.stdin.readline
INF = int(1e9)   # 무한대를 표현하기 위한 초기화

v, e = map(int, input().split())   # 노드와 간선 입력
start = int(input())   # 시작노드 입력
graph = [[] for _ in range(v + 1)]   # graph 테이블 초기화
distance = [INF] * (v + 1)   # distance 테이블 무한대 초기화

# 그래프 입력
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 다익스트라 알고리즘 매서드
def dijkstra(start):
    q = []   # 큐 테이블 생성
    heapq.heappush(q, (0, start))   # 첫번째 시작노드, 간선비용 초기화
    distance[start] = 0
    while q:   # 큐 원소가 모두 pop 되기 전까지
        dist, now = heapq.heappop(q)   # 큐 에서 가장 최소 간선비용 가지는 노드 pop
        if dist > distance[now]:   # 새로 pop 한 간선비용이 더 비싸면 무시
            continue
        for i in graph[now]:   # pop 한 graph 방문
            cost = dist + i[1]   # cost -> 최신회된 간선비용 + 기존 이전의 간선비용
            if cost < distance[i[0]]:   # cost 비용이 현재 노드까지의 간선비용보다 값 싸면
                distance[i[0]] = cost   # distance 초기화
                heapq.heappush(q, (cost, i[0]))   # heap 자료구조 다시 최신화

# 결과출력
dijkstra(start)
for i in range(1, v + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])