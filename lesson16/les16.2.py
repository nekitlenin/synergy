class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s <= 1:
            raise ValueError("Шаг не может быть меньше или равен 0")
        self.s -= 1

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        moves_x = (dx + self.s - 1) // self.s
        moves_y = (dy + self.s - 1) // self.s
        return moves_x + moves_y


def main_turtle():
    t = Turtle()
    print(f"Начальная позиция черепашки: ({t.x}, {t.y}), шаг: {t.s}")

    while True:
        print("\nТекущая позиция:", (t.x, t.y), "Шаг:", t.s)
        print("Выберите действие:")
        print("1 - Вверх")
        print("2 - Вниз")
        print("3 - Влево")
        print("4 - Вправо")
        print("5 - Увеличить шаг (evolve)")
        print("6 - Уменьшить шаг (degrade)")
        print("7 - Посчитать минимальное количество ходов до точки")
        print("0 - Выход")
        choice = input("Введите номер действия: ")

        if choice == "1":
            t.go_up()
            print("Черепашка пошла вверх")
        elif choice == "2":
            t.go_down()
            print("Черепашка пошла вниз")
        elif choice == "3":
            t.go_left()
            print("Черепашка пошла влево")
        elif choice == "4":
            t.go_right()
            print("Черепашка пошла вправо")
        elif choice == "5":
            t.evolve()
            print("Шаг увеличен на 1")
        elif choice == "6":
            try:
                t.degrade()
                print("Шаг уменьшен на 1")
            except ValueError as e:
                print("Ошибка:", e)
        elif choice == "7":
            try:
                x2 = int(input("Введите координату x2: "))
                y2 = int(input("Введите координату y2: "))
                moves = t.count_moves(x2, y2)
                print(f"Минимальное количество ходов до ({x2}, {y2}): {moves}")
            except ValueError:
                print("Ошибка: введите целые числа")
        elif choice == "0":
            print("Выход из программы Черепашка")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

main_turtle()
