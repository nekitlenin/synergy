def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_sequence(n):
    start_factorial = factorial(n)
    
    result = []
    for i in range(start_factorial, 0, -1):
        result.append(factorial(i))
    
    return result

number = int(input("Введите натуральное число: "))
result_list = factorial_sequence(number)
print(f"Факториал числа {number}: {factorial(number)}")
print(f"Список факториалов: {result_list}")