# 두 배열의 원소 교체
n, k = map(int, input().split())

list_a = list(map(int, input().split()))   # 배열 입력받기
list_b = list(map(int, input().split()))   # 배열 입력받기

list_a.sort()  # 오름차순 정렬
list_b.sort(reverse=True)   # 내림차순 정렬

for i in range(k):   # k 번째 요소까지
    if list_a[i] < list_b[i]:   # 값 비교했을때 list_b 의 원소가 더 크면
        list_a[i] = list_b[i]   # 인덱스 값 교환
    else:   # 값 비교했을때 list_a 의 원소가 더 크면
        break

print(sum(list_a))   # 답안출력

