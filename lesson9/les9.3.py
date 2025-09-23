# Ввод последовательности чисел
numbers = list(map(int, input().split()))

# Множество для отслеживания уже встреченных чисел
seen = set()

# Проверяем каждое число
for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)  # Добавляем число в множество встреченных