N = int(input())
arr = list(map(int, input().split()))

if N > 0:
    new_arr = [arr[-1]]
    new_arr.extend(arr[:-1])
else:
    new_arr = []

# Выводим результат
print(' '.join(map(str, new_arr)))