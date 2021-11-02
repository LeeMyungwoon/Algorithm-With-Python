# 선택정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]   # 정렬되어 있지 않은 리스트

for i in range(len(array)):
    min_array = i   # 인덱스의 가장 첫번째를 임의로 최소값으로 초기화
    for j in range(i + 1, len(array)):   # 정렬 완료된 인덱스는 제외해야 하기 때문에 i + 1 번째 인덱스부터 시작
        if array[min_array] > array[j]:   # 정렬되지 않은 인덱스 중 가장 작은값 찾기
            min_array = j   # 가장작은 값 최소값으로 초기회
    array[i], array[min_array] = array[min_array], array[i]   # 가장 작은숫자 앞으로 이동, 스와핑
print(array)