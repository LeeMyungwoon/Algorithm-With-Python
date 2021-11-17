# 효율적인 화폐구성

n, m = map(int, input().split())
coin_type = []   # 화폐의 종류
for i in range(n):
    coin_type.append(int(input()))
d = [10001] * (m + 1)   # (m + 1)크기의 dp 테이블 10001 초기화 (무한대)
d[0] = 0   # 총 액수가 0원이면 0이기 때문에 0으로 초기화

for i in range(n):   # i = 화폐의 종류
    for j in range(coin_type[i], m + 1):   # j = 액수
        if d[j - coin_type[i]] != 10001:
            d[j] = min(d[j], d[j - coin_type[i]] + 1)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])   # 답안출력