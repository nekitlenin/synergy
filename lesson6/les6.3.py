A = int(input("Введите A: "))
B = int(input("Введите B: "))

even_numbers = []

for num in range(A, B + 1):
    if num % 2 == 0:
        even_numbers.append(str(num))

print(" ".join(even_numbers))