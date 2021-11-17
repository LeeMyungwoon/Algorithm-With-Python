# 개미전사

n = int(input())
array = list(map(int, input().split()))
d = [0] * 1001   # dp 테이블 초기화

d[0] = array[0]   # d[0] 은 0번째 인덱스 밖에 없으니 0번째 인덱스로 초기화
d[1] = max(array[0], array[1])   # d[1] 은 0번째 인덱스와 1번째 인덱스 중 큰 값을 골라 초기화

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])   # 답안출력