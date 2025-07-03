# tests.py

from main import Person, Rectangle, BankAccount, Car, Point

def test_person():
    # TODO: Создай объект с именем "Alice", возрастом 30, полом "female"
    # TODO: Вызови метод greet и проверь результат
    pass

def test_rectangle():
    # TODO: Прямоугольник 3x4 → площадь 12, периметр 14
    pass

def test_bank_account():
    # TODO: Пополнить счёт, снять часть, проверить остаток
    pass

def test_car():
    # TODO: Создай объект и проверь start_engine()
    pass

def test_point():
    # TODO: Сравни точки по расстоянию
    pass

def run_tests():
    test_person()
    test_rectangle()
    test_bank_account()
    test_car()
    test_point()
    print("✅ Все тесты пройдены")

if __name__ == "__main__":
    run_tests()