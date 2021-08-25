# 큰 수의 법칙
# 내가 푼 답안
threeInput = input().split() # N, M, K 입력받기
array = input().split() # 배열 값 입력받기
a = 0 # K값을 임의로 만들기
sum = 0
for i in range(3): # N, M, K값 int로 형 변환
    threeInput[i] = int(threeInput[i])
for i in range(threeInput[0]): # 배열값 int로 형 변환
    array[i] = int(array[i])

array.sort(reverse=1) # 오름차순으로 정렬
for i in range(threeInput[1]): 
    if a < 3: # K값이 3이 될때 까지만 가장 큰 수 더하기
        sum += array[0]
        a += 1
    else: # K값이 3을 채우고 난 후에는 두번째로 큰 수 한번 더하기
        sum += array[1]
        a = 0
print(sum) # 답안 출력
########################################################################################################################
# 모범답안
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 k번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할때 마다 1씩 빼기
    if m == 0: # m이 0이라면 반복문 탈출
        break
    result += second # 2번째로 큰 수 한 번 더하기
    m -= 1 # 더할 때 마다 1씩 빼기

print(result) # 최종 답안 출력
########################################################################################################################
# 더 효율적으로 코드 짜기

#N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k      # (k + 1)은 수열의 길이, m / (k + 1)은 총 반복되는 수열의 횟수, m / (k + 1)은 가장 큰 수가 나오는 총 횟수
count += m % (k + 1)              # m / (k + 1)의 값이 정수로 안떨어 질 수 도 있어서 나머지까지 더해준다

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)
########################################################################################################################

# 보완할점1: map함수를 잘 이용하여 입력값을 한줄로 처리하기
# 보완할점2: 'a'라는 새로운 변수를 만들지 말고, 이미 입력값으로 나온 K값을 활용하기( - 이용하여)