# 게임 개발
# 내가 푼 답안

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

list_map = [[0] * m] * n
for i in range(n):
    list_map[i] = list(map(int, input().split()))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # 북쪽, 남쪽, 서쪽, 동쪽
direction_list = [0, 1, 2, 3]   # 북쪽, 동쪽, 남쪽, 서쪽


print(list_map)
print(x, y, direction)