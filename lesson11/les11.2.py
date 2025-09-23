import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return "года"
    else:
        return "лет"

def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False

def create():
    if pets:
        last = collections.deque(pets, maxlen=1)[0]
        new_id = last + 1
    else:
        new_id = 1
    
    pet_name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    pet_age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")
    
    pets[new_id] = {
        pet_name: {
            "Вид питомца": pet_type,
            "Возраст питомца": pet_age,
            "Имя владельца": owner_name
        }
    }
    print(f"Запись добавлена с ID: {new_id}")

def read(ID):
    pet_info = get_pet(ID)
    if not pet_info:
        print("Питомец с таким ID не найден")
        return
    
    pet_name = list(pet_info.keys())[0]
    data = pet_info[pet_name]
    
    suffix = get_suffix(data["Возраст питомца"])
    info = f'Это {data["Вид питомца"].lower()} по кличке "{pet_name}". Возраст питомца: {data["Возраст питомца"]} {suffix}. Имя владельца: {data["Имя владельца"]}'
    print(info)

def update(ID):
    pet_info = get_pet(ID)
    if not pet_info:
        print("Питомец с таким ID не найден")
        return
    
    pet_name = list(pet_info.keys())[0]
    data = pet_info[pet_name]
    
    print("Введите новые данные (оставьте пустым, чтобы не изменять):")
    
    new_type = input(f"Вид питомца [{data['Вид питомца']}]: ") or data['Вид питомца']
    new_age = input(f"Возраст питомца [{data['Возраст питомца']}]: ") or data['Возраст питомца']
    new_owner = input(f"Имя владельца [{data['Имя владельца']}]: ") or data['Имя владельца']
    
    pets[ID][pet_name]["Вид питомца"] = new_type
    pets[ID][pet_name]["Возраст питомца"] = int(new_age)
    pets[ID][pet_name]["Имя владельца"] = new_owner
    
    print("Данные обновлены")

def delete(ID):
    if ID not in pets:
        print("Питомец с таким ID не найден")
        return
    
    pet_name = list(pets[ID].keys())[0]
    del pets[ID]
    print(f"Питомец {pet_name} (ID: {ID}) удален")

def pets_list():
    if not pets:
        print("База данных пуста")
        return
    
    print("\n=== СПИСОК ПИТОМЦЕВ ===")
    for ID, pet_info in pets.items():
        pet_name = list(pet_info.keys())[0]
        data = pet_info[pet_name]
        suffix = get_suffix(data["Возраст питомца"])
        print(f"ID: {ID} - {data['Вид питомца']} '{pet_name}', возраст: {data['Возраст питомца']} {suffix}, владелец: {data['Имя владельца']}")

def main():
    print("Добро пожаловать в базу данных ветеринарной клиники!")
    print("Доступные команды: create, read, update, delete, list, stop")
    
    command = ""
    while command != 'stop':
        command = input("\nВведите команду: ").lower()
        
        if command == 'create':
            create()
        elif command == 'read':
            ID = int(input("Введите ID питомца: "))
            read(ID)
        elif command == 'update':
            ID = int(input("Введите ID питомца для обновления: "))
            update(ID)
        elif command == 'delete':
            ID = int(input("Введите ID питомца для удаления: "))
            delete(ID)
        elif command == 'list':
            pets_list()
        elif command == 'stop':
            print("Работа программы завершена")
        else:
            print("Неизвестная команда")

if __name__ == "__main__":
    main()