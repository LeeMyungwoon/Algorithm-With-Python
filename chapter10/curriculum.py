# 커리큘럼

from collections import deque   # queue 자료구조 사용을 위한 import
import copy   # 리스트 copy 를 위한 import

# v = 과목의 수
v = int(input())
graph = [[] for _ in range(v + 1)]
indegree = [0] * (v + 1)
time = [0] * (v + 1)

# 노드, 간선, 진입노드, 강의시간 입력
for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]   # data[0]에 강의시간정보 있으므로 time table에 초기화
    for x in data[1:-1]:
        graph[x].append(i)   # graph 간선, 노드 초기화
        indegree[i] += 1   # 진입노드 +1

# 위상정렬 매서드
def topology_sort():
    q = deque()
    result = copy.deepcopy(time)

    # 진입노드가 0이 있다면 queue에 append
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:   # queue 의 원소가 없어질 때 까지
        now = q.popleft()   # queue 에서 pop
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])   # 현재 노드의 강의시간은 (기존 저정되있던 시간) 과 (이전노드 강의시간 + 현재시간) 비교하여 큰값으로 초기화
            indegree[i] -= 1   # 현재노드의 진입노드 -1

            # 진입노드가 0인 노드가 있다면 queue에 append
            if indegree[i] == 0:
                q.append(i)

    # 결과출력
    for i in range(1, v + 1):
        print(result[i])

topology_sort()   # 함수호출