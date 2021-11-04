# 선택 정렬
array = [6, 3, 7, 2, 9, 5, 1, 4, 8, 0]
for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
print(array)

# 삽입 정렬
array = [6, 3, 7, 2, 9, 5, 1, 4, 8, 0]
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
        else:
            break
print(array)
# 퀵 정렬
# 계수 정렬
