number = int(input("Введите пятизначное число: "))

digit_10000 = number // 10000
digit_1000 = (number // 1000) % 10
digit_100 = (number // 100) % 10
digit_10 = (number // 10) % 10
digit_1 = number % 10

step1 = digit_10 ** digit_1
step2 = step1 * digit_100

result = step2 / (digit_10000 - digit_1000)

print(f"Результат: {result}")