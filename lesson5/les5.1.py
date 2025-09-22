number = int(input("Введите целое число: "))

if number == 0:
    print("нулевое число")
else:
    if number > 0:
        sign = "положительное"
    else:
        sign = "отрицательное"
    
    if number % 2 == 0:
        parity = "четное"
        print(f"{sign} {parity} число")
    else:
        print("число не является четным")