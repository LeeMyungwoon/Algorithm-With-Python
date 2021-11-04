# 계수정렬
array = [2, 5, 6, 8, 2, 5, 2, 8, 9, 0, 1, 34, 8, 2, 5, 8, 9, 1, 12]

# 데이터 담을 count 리스트 생성
count = [0] * (max(array) + 1)
for i in range(len(array)):
    count[array[i]] += 1   # 각 인덱스에 맞는것 +1 씩 추가

for i in range(len(count)):
    for j in range(count[i]):   # 각 인덱스에 해당하는 숫자만큼 출력
        print(i, end = ' ')