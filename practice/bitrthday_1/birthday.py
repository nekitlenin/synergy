from datetime import datetime


def get_date_input():
    """Запрашивает у пользователя дату рождения"""
    day = int(input("Введите день рождения (число): "))
    month = int(input("Введите месяц рождения (число): "))
    year = int(input("Введите год рождения: "))
    return day, month, year


def day_of_week(day, month, year):
    """Определяет день недели по дате рождения"""
    date = datetime(year, month, day)
    days = [
        "Понедельник", "Вторник", "Среда",
        "Четверг", "Пятница", "Суббота", "Воскресенье"
    ]
    return days[date.weekday()]


def is_leap_year(year):
    """Определяет, является ли год високосным"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def calculate_age(day, month, year):
    """Определяет текущий возраст пользователя"""
    today = datetime.today()
    age = today.year - year
    if (today.month, today.day) < (month, day):
        age -= 1
    return age


# Шаблоны цифр для "табло" (5 строк x 3 столбца на цифру)
DIGITS = {
    '0': ["***", "* *", "* *", "* *", "***"],
    '1': ["  *", "  *", "  *", "  *", "  *"],
    '2': ["***", "  *", "***", "*  ", "***"],
    '3': ["***", "  *", "***", "  *", "***"],
    '4': ["* *", "* *", "***", "  *", "  *"],
    '5': ["***", "*  ", "***", "  *", "***"],
    '6': ["***", "*  ", "***", "* *", "***"],
    '7': ["***", "  *", "  *", "  *", "  *"],
    '8': ["***", "* *", "***", "* *", "***"],
    '9': ["***", "* *", "***", "  *", "***"],
    ' ': ["   ", "   ", "   ", "   ", "   "],
}


def print_star_date(day, month, year):
    """Выводит дату в формате 'дд мм гггг' звёздочками, как на табло"""
    date_str = f"{day:02d} {month:02d} {year:04d}"

    rows = ["", "", "", "", ""]
    for char in date_str:
        symbol = DIGITS.get(char, DIGITS[' '])
        for i in range(5):
            rows[i] += symbol[i] + "  "

    print("\nДата рождения на электронном табло:\n")
    for row in rows:
        print(row)


def main():
    day, month, year = get_date_input()

    print(f"\nВы родились в {day_of_week(day, month, year)}")

    if is_leap_year(year):
        print(f"{year} год был високосным")
    else:
        print(f"{year} год не был високосным")

    age = calculate_age(day, month, year)
    print(f"Вам сейчас {age} лет")

    print_star_date(day, month, year)


if __name__ == "__main__":
    main()
    