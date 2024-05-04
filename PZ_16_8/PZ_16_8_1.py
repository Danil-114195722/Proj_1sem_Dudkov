"""
Создайте класс "Человек" с атрибутами "имя", "возраст" и "пол". Напишите метод,
который выводит информацию о человеке в формате "Имя: имя, Возраст: возраст, Пол: пол".
"""


class Human:
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def info(self) -> None:
        print(f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}")


test_human = Human(name="Test", age=100500, gender="F")
test_human.info()
