class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

Autobus = Transport("Renaul Logan", 180, 12)

print(f"Название автомобиля: {Autobus.name} Скорость: {Autobus.max_speed} Пробег: {Autobus.mileage}")
