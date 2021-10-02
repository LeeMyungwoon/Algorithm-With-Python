# 숫자 카드게임
# 내가 푼 답안

# n, m -> 행, 열 크기 입력
n, m = map(int, input().split())
card_List = [[0] * m] * n

for i in range(n):
    card_List[i] = list(map(int, input().split()))

comparison_List = [0] * n   # 값을 비교하기 위해 새로운 배열 선언

for i in range(n):
    for j in range(m):
        card_List[i].sort()    # 2차원배열을 각각 오름차순으로 정렬
    comparison_List[i] = card_List[i][0]

    
print(comparison_List[-1])   # 결과 출력
#########################################################################################
# py.min()함수를 이용하는 답안

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)   # 최종 답안 출력
#########################################################################################
# 2중 반복문구조 이용하는 답안

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중애서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)   # 최종 답안 출력
#########################################################################################

# 보완할점1: 필요없는 배열을 만들어 메모리를 사용하지 말자 (이미 만들어놓은 배열을 계속 초기화 하여 사용가능하다)