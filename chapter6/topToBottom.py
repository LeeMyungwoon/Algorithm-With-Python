# 위에서 아래로

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort(reverse=True)
for i in range(n):
    print(array[i], end = ' ')