N = int(input("Введите количество чисел: "))

count_zero = 0

for i in range(N):
    num = int(input(f"Введите число {i+1}: "))
    if num == 0:
        count_zero += 1

print(f"Количество чисел, равных нулю: {count_zero}")