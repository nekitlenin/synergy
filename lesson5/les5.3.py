X = int(input("Минимальная сумма инвестиций: "))
A = int(input("Сумма у Майкла: "))
B = int(input("Сумма у Ивана: "))

mike_can = A >= X
ivan_can = B >= X
together_can = (A + B) >= X

if mike_can and ivan_can:
    print(2)
elif mike_can:
    print("Mike")
elif ivan_can:
    print("Ivan")
elif together_can:
    print(1)
else:
    print(0)