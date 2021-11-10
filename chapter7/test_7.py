# 스택구현, 큐 구현, 선택정렬 구현, 삽입정렬 구현, 퀵정렬 구현(재귀함수), 퀵정렬 구현(리스트컴프리헨션, 리스트슬라이싱), 계수정렬 구현, 이진탐색 구현(재귀함수), 이진탐색 구현(반복문)
# 데이터 수 1,000만 이상 데이터 범위 1,000억 이상 일때 입력 처리

# 떡볶이 떡 만들기, 이진탐색
n, m = map(int, input().split())   # n = 떡의 개수, m = 요청한 떡의 길이
array = list(map(int, input().split()))   # 현재 존재하는 떡의 길이

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    # 떡의 양이 부족할 경우 -> 더 많이 잘라야 하기 때문에 왼쪽 영역에서 탐색
    if total < m:
        end = mid - 1
    # 떡의 양이 충분할 경우 -> 더 적게 잘라야 하기 때문에 오른쪽 영역에서 탐색
    else:
        result = mid   # 최대한 덜 잘라야 하기 때문에 이 부분에서 result 기록
        start = mid + 1
print(result)