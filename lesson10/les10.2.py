# Создаем пустой словарь
my_dict = {}

# Заполняем словарь с помощью цикла
for i in range(10, -6, -1):  # от 10 до -5 включительно
    my_dict[i] = i ** i

# Выводим результат
for key, value in my_dict.items():
    print(f"{key}: {value}")