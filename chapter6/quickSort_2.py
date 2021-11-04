# 퀵 정렬
# 리스트 슬라아싱, 리스트 컴프리헨션 이용
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:   # 정렬해야할 원소의 개수가 1이하면 지금까지 정렬된 리스트 반환
        return array
    pivot = array[0]   # 제일 첫번째 원소를 피벗값으로 설정
    tail = array[1:]   # 피벗을 제외한 나머지 리스트

    left_side = [x for x in tail if x <= pivot]   # 피벗 값보다 작은 원소들 -> left_side
    right_side = [x for x in tail if x > pivot]   # 피벗 값보다 큰 원소들 -> right_side

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)   # 재귀함수 이용

# 정렬된 리스트 출력
print(quick_sort(array))