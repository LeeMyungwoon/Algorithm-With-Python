# 다익스트라 최단경로 알고리즘

import sys
input = sys.stdin.readline   # 데이터의 수를 많이 받는다 가정해서 치환
INF = int(1e9)   # 무한을 표현하기 위해서 10억 정의

v, e = map(int, input().split())
start = int(input())   # 시작노드 입력
graph = [[] for _ in range(v + 1)]   # 그래프 초기화
visited = [False] * (v + 1)   # 방문 안했다는 가정하에 모두 False 값으로 초기화
distance = [INF] * (v + 1)  # 간선비용 무한으로 초기화

for _ in range(e):
    a, b, c = map(int, input().split())   # a 노드에서 b 노드로 갈때 간선비용 c
    graph[a].append((b, c))

# 최소 인덱스 값 반환 매서드
def smallest_index():
    small_index = INF   # 가장 최소값 무한으로 초기화
    index = 0
    for i in range(1, v + 1):
        if distance[i] < small_index and not visited[i]:   # 현재의 거리가 small_index 보다 작고, 방문하지 않았다면
            small_index = distance[i]   # 현재 거리 -> small_index 로 초기화
            index = i
    return index   # 인덱스 값 반환

# 다익스트라 알고리즘 매서드
def dijkstra(start):
    distance[start] = 0   # 시작노드 간선비용 0으로 초기화 (자기자신)
    visited[start] = True   # 시작노드 방문처리
    for j in graph[start]:
        distance[j[0]] = j[1]   # 시작노드로 부터 인접한 노드까지의 간선비용 초기화
    for i in range(v - 1):
        now = smallest_index()   # 최소 간선비용 가진 now 인덱스 반환
        visited[now] = True   # 인덱스 now 노드 방문처리
        for j in graph[now]:
            cost = distance[now] + j[1]   # cost = 이전노드에서의 간선비용 + 현재노드까지의 간선비용
            if cost < distance[j[0]]:   # cost 값이 이전의 정의된 간선비용보다 작을 때 최소값 초기화
                distance[j[0]] = cost

dijkstra(start)   # 다익스트라 매서드 호출

# 출력
for i in range(1, v + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])