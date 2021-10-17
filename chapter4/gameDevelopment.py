# 게임 개발
# 내가 푼 답안

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

d = [[0 * x for i in range(n)] for x in range(m)]
d[x][y] = 1   # 방문처리

# 맵 리스트 업로드
array = [] 
for _ in range(n):
    array.append(list(map(int, input().split())))

# 북쪽, 동쪽, 남쪽, 서쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1] 

# 방향 전환 함수선언
def change_dir():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:

    change_dir()   # 완쪽으로 회전
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 회전 후 안가본 칸 존재할 때
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1   # 방문처리
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    
    # 회전 후 가본곳이거나 바다일 떄
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        if d[nx][ny] == 0:
            x = nx
            y = ny
        else:
            turn_time = 0
            break
print(count)