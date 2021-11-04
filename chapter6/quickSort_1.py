# 퀵 정렬
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(array, start, end):
    pivot = start
    left = start + 1
    right = end

    # 원소의 개수가 1개라면 탈출
    if start >= end:
        return

    # 겹치지 않을 때 까지만
    while left <= right:

        # pivot 보다 큰 수 찾기
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # pivot 보다 작은 수 찾기
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 겹쳤을 경우
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]

        # 겹치지 않았을 경우
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)   # 기존 피벗기준 왼쪽 리스트 재귀함수 호출
    quick_sort(array, right + 1, end)   # 기존 피벗기준 오른쪽 리스트 재귀함수 호출

# array(정렬하고자 하는 배열, 시작하는 인덱스, 끝나는 인덱스)
quick_sort(array, 0, len(array) - 1)
# 정렬된 배열 출력
print(array)