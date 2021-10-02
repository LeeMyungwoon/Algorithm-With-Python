# 1이 될 때까지
# 내가 푼 답안

# N, K를 입력받음
n, k = map(int, input().split())

result = 0
while (True):
    if (n % k != 0):   # N이 K로 나눠지지 않을때 N에서 1씩 뺀다
        n -= 1
        result += 1   # 이 사이클 한번 돌때마다 result 값 1씩 추가
    else:   # N이 K로 나눠지면 나눈다
        n = n / k
        result += 1   # 이 사이클 한번 돌떄마다 result 값 1씩 추가
    if (n == 1):
      break   # N이 최종 1이되면 while 문 탈출
# 최종답안 출력
print(result)
#########################################################################################
# 단순하게 푸는 답안 예시

n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)
#########################################################################################
# N이 100억 이상의 큰 수가 되는 경우일때 효율적인 소스코드

# N, K를 공백으로 구분하여 입력받기
n, m = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
#########################################################################################
