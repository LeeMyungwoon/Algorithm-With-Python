# 왕실의 나이트
# 내가 푼 답안

input_value = input()
x = input_value[:-1]
y = int(input_value[1:])
result = 0

a = [2, -2]
b = [1, -1]

for i in a:
    for j in b:
        dx = ord(x) + i
        dy = y + j
        if (dx < 97 or dx > 104) or (dy <= 0 or dy > 8):
            continue
        result += 1

        dx = ord(x) + j
        dy = y + i
        if (dx < 94 or dx > 104) or (dy <= 0 or dy > 8):
            continue
        result += 1

print(result)
##########################################################################
# 답안 예시

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 0 and next_column <= 8:
        result += 1

print(result)
##########################################################################
# 보완할점1: [(x, y)] -> 튜플형태를 활용해야한다
# 보완할점2: 문자열은 배열의 형태를 띄기 때문에 이를 잘 활용하여 입력을 받아야 한다
#            ex) input = a1 -> input[0] = a, input[1] = 1

