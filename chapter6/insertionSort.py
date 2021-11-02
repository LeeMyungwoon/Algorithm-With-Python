# 삽입정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]   # 정렬되어 있지 않은 리스트

for i in range(1, len(array)):   # 0 번째 인덱스는 정렬이 되어있다고 판단하여 1 번째 인덱스부터 판단
    for j in range(i, 0, -1):   # i 번째 인덱스 부터 1번째 인덱스까지 비교하여 가장 작은 숫자가 앞으로 이동
        if array[j] < array[j - 1]:   # j 번째 인덱스보다 j - 1 번째 인덱스가 크면
            array[j - 1], array[j] = array[j], array[j - 1]   # 두 인덱스 스와핑
        else:
            break   # 자기보다 작은데이터 만나면 그자리에서 멈춤
print(array)