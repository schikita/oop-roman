# tests.py

from main import Person, Rectangle, BankAccount, Car, Point

def test_person():
    p = Person('Alice', 30, 'female')

    assert p.name == 'Alice'
    assert p.age == 30
    assert p.gender == "female"

    assert p.greet() == "Hi, I'm Alice, 30 years old."

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
    # test_rectangle()
    test_bank_account()
    test_car()
    test_point()
    print("✅ Все тесты пройдены")

if __name__ == "__main__":
    run_tests()