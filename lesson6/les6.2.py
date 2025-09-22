X = int(input("Введите натуральное число: "))

count_divisors = 0

for i in range(1, int(X**0.5) + 1):
    if X % i == 0:
        count_divisors += 1
        if i != X // i:
            count_divisors += 1

print(f"Количество натуральных делителей числа {X}: {count_divisors}")