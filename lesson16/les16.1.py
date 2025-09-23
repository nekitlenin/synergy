class Kassa:
    def __init__(self):
        self.amount = 0  # текущее количество денег в кассе

    def top_up(self, X):
        self.amount += X

    def count_1000(self):
        return self.amount // 1000  # сколько целых тысяч осталось

    def take_away(self, X):
        if X > self.amount:
            raise ValueError("Недостаточно денег в кассе")
        self.amount -= X


def main_kassa():
    k = Kassa()
    while True:
        print("\nТекущий баланс:", k.amount)
        print("Выберите действие:")
        print("1 - Пополнить кассу")
        print("2 - Узнать количество целых тысяч")
        print("3 - Снять деньги")
        print("0 - Выход")
        choice = input("Введите номер действия: ")

        if choice == "1":
            try:
                x = int(input("Введите сумму для пополнения: "))
                k.top_up(x)
                print(f"Касса пополнена на {x}")
            except ValueError:
                print("Ошибка: введите целое число")
        elif choice == "2":
            print("Целых тысяч в кассе:", k.count_1000())
        elif choice == "3":
            try:
                x = int(input("Введите сумму для снятия: "))
                k.take_away(x)
                print(f"Снято {x} из кассы")
            except ValueError as e:
                print("Ошибка:", e)
        elif choice == "0":
            print("Выход из программы Касса")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

main_kassa()
