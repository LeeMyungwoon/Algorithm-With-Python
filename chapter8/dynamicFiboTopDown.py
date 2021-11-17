# 피보나치 수열 다이나믹 프로그래밍 탑다운 (재귀함수 이용)
d = [0] * 100
def fivo(num):
    if num == 1 or num == 2:   # 1번째나 2번째 피보나치 수열일 경우
        return 1
    if d[num] != 0:   # 이미 계산한 순서의 피보나치 수열일 경우
        return d[num]
    d[num] = fivo(num - 1) + fivo(num - 2)   # 아직 계산하지 않은 피보나치 수열일 경우
    return d[num]
print(fivo(99))   # 99 번째 피보나치 수열 출력