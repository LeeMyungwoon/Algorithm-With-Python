# 떡볶이 떡 만들기

# n = 떡의 갯수, m = 요청한 떡의 길이
n, m = map(int, input().split())

cake_list = list(map(int, input().split()))
cake_list.sort(reverse=True)   # 있는 떡 리스트 정렬

def cake_cut(array, num):
    add = 0
    while add < m:
        add = 0
        for i in range(len(array)):
            if array[i] > num:
                add += array[i] - num
            else:
                break
        num -= 1
    return num + 1

print(cake_cut(cake_list, (max(cake_list) - 1)))

# 데이터의 범위가 크고, 데이터의 수 범위 역시 크기 때문에 이진탐색을 이용하여 문제풀이 해야한다

