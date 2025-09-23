# Создаем пустой словарь
pets = {}

# Ввод информации о питомце
pet_name = input("Введите имя питомца: ")
pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

# Определяем правильное окончание для возраста
if pet_age % 10 == 1 and pet_age % 100 != 11:
    age_word = "год"
elif 2 <= pet_age % 10 <= 4 and (pet_age % 100 < 10 or pet_age % 100 >= 20):
    age_word = "года"
else:
    age_word = "лет"

# Заполняем словарь
pets[pet_name] = {
    'Вид питомца': pet_type,
    'Возраст питомца': pet_age,
    'Имя владельца': owner_name
}

# Выводим информацию о питомце
pet_info = pets[pet_name]
print(f'Это {pet_info["Вид питомца"].lower()} по кличке "{pet_name}". Возраст питомца: {pet_info["Возраст питомца"]} {age_word}. Имя владельца: {pet_info["Имя владельца"]}')