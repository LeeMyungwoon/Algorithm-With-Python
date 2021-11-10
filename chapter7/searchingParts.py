# 부품찾기

# n 입력받기
n = int(input())
existence_parts = list(map(int, input().split()))
m = int(input())
require_parts = list(map(int, input().split()))

def searching(array, target, start, end):
    if start > end:
        return "no"
    mid = (start + end) // 2

    # 중간값이 타겟과 일치할 때
    if array[mid] == target:
        return "yes"

    # 타겟이 중간값 보다 작을 때
    elif array[mid] > target:
        return searching(array, target, start, (mid - 1))

    # 타겟이 중간값 보다 클 때
    else:
        return searching(array, target, (mid + 1), end)


# 이진탐색을 위한 오름차순 정렬
existence_parts.sort()

for i in range(m):
    result = searching(existence_parts, require_parts[i], 0, (len(existence_parts) - 1))
    print(result, end = ' ')

# 계수정렬을 이용해서도 풀 수 있다
# 집합 자료형을 이용해서도 풀 수 있다