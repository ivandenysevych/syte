# Базовий клас
class Vehicle:
    def __init__(self, brand):
        # Конструктор, що приймає назву бренду транспортного засобу
        self.brand = brand

    def move(self):
        # Абстрактний метод, що має бути реалізований у підкласах
        raise NotImplementedError("Subclass must implement abstract method")

# Підклас 1: Автомобіль
class Car(Vehicle):
    def move(self):
        # Реалізація методу move для автомобіля
        return f"The {self.brand} car drives on the road."

# Підклас 2: Велосипед
class Bicycle(Vehicle):
    def move(self):
        # Реалізація методу move для велосипеда
        return f"The {self.brand} bicycle rides on the bike path."

# Підклас 3: Літак
class Airplane(Vehicle):
    def move(self):
        # Реалізація методу move для літака
        return f"The {self.brand} airplane flies in the sky."

# Створення об'єктів різних транспортних засобів
car = Car("Toyota")            # Створюємо об'єкт автомобіля
bicycle = Bicycle("Giant")      # Створюємо об'єкт велосипеда
airplane = Airplane("Boeing")   # Створюємо об'єкт літака

# Виклик методів для демонстрації наслідування
print(car.move())        # Виведе: The Toyota car drives on the road.
print(bicycle.move())    # Виведе: The Giant bicycle rides on the bike path.
print(airplane.move())   # Виведе: The Boeing airplane flies in the sky.

# Функція для демонстрації поліморфізму
def vehicle_move(vehicle):
    # Функція приймає об'єкт типу Vehicle і викликає його метод move
    print(vehicle.move())

# Виклик функції для різних транспортних засобів
vehicle_move(car)       # Виведе: The Toyota car drives on the road.
vehicle_move(bicycle)   # Виведе: The Giant bicycle rides on the bike path.
vehicle_move(airplane)  # Виведе: The Boeing airplane flies in the sky.
