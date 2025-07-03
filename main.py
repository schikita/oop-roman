# classes.py

# Задание 1: Класс "Человек"
class Person:
    def __init__(self, name: str, age: int, gender: str):
        # TODO: Сохрани имя, возраст и пол в атрибутах экземпляра
        pass

    def greet(self):
        # TODO: Верни строку вида "Hi, I'm {name}, {age} years old."
        pass


# Задание 2: Класс "Прямоугольник"
class Rectangle:
    def __init__(self, width: float, height: float):
        # TODO: Сохрани ширину и высоту
        pass

    def area(self):
        # TODO: Верни площадь прямоугольника
        pass

    def perimeter(self):
        # TODO: Верни периметр прямоугольника
        pass


# Задание 3: Класс "БанкСчет" с инкапсуляцией
class BankAccount:
    def __init__(self):
        # TODO: Приватный атрибут _balance = 0
        pass

    def deposit(self, amount: float):
        # TODO: Увеличь баланс на сумму
        pass

    def withdraw(self, amount: float):
        # TODO: Уменьши баланс, если хватает средств
        pass

    def get_balance(self):
        # TODO: Верни текущий баланс
        pass


# Задание 4: Класс "Автомобиль"
class Car:
    def __init__(self, brand: str, model: str, year: int):
        # TODO: Сохрани переданные параметры как атрибуты
        pass

    def start_engine(self):
        # TODO: Верни строку "Engine of {brand} {model} started."
        pass


# Задание 5: Класс "Точка"
import math

class Point:
    def __init__(self, x: float, y: float):
        # TODO: Сохрани координаты x и y
        pass

    def distance_to_origin(self):
        # TODO: Верни расстояние до (0, 0)
        pass

    def __lt__(self, other):
        # TODO: Сравнение по расстоянию до начала координат
        pass

    def __eq__(self, other):
        # TODO: Сравнение по расстоянию до начала координат
        pass