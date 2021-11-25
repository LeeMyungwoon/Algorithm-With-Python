import heapq

# 오름차순 힙 정제
def heapsort(iterable):
    h = []
    result = []
    # 모든원소 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 원소 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# 내림차순 힙 정제 -> 기본적으로 파이썬에서는 최대힙을 제공해주지는 않는다 (최소힙에서 부호를 바꿔서 구현가능)
def heapsort(iterable):
    h = []
    result = []
    # 모든원소 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)   # 내림차순 정렬 하려면 부호를 바꿔주면 된다
    # 힙에 삽입된 원소 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))   # 내림차순 정렬 하려면 부호를 바꿔주면 된다
    return result
result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

