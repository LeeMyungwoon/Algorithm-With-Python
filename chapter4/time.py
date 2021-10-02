# 시각

# 내가 푼 답안

time = int(input())
result = 0
for i in range (time + 1):
    for j in range (60):
        for k in range (60):
            if '3' in str(i) or str(j) or str(k):   # -> if '3' in str(i) or '1' in str(j) or '1' in str(k)
                result += 1
print(result)
################################################################################
# 답안 예시

# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3' 이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)   # 답안출력
################################################################################
# 보완할점1: 완전탐색이므로 시간복잡도를 고려했을 때 탐색해야 할 데이터의 수가 100만 개 이하일때 사용 시 적절
# 보완할점2: 연산자는 bool 타입 연산자이지, 비교 연산자가 아니라는 것

