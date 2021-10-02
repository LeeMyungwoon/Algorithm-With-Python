# 상하죄우

num = int(input())
plans = list(map(str, input().split()))

x, y = 1, 1
move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for i in range(len(move_types)):
        if move_types[i] == plan:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > num or ny < 1 or ny > num:
        continue
    x, y = nx, ny

# 답안출력
print(x, y)
