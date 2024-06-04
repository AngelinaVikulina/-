# Создайте класс "Фрукт", который содержит информацию о наименовании и весе
# фрукта. Создайте классы "Яблоко" и "Апельсин", которые наследуются от класса
# "Фрукт" и содержат информацию о цвете.
class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Apple(Fruit):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color

class Orange(Fruit):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color


apple = Apple("Яблоко", 150, "красное")
orange = Orange("Апельсин", 200, "оранжевый")

print(f"{apple.name} весит {apple.weight} грамм, цвета {apple.color}")
print(f"{orange.name} весит {orange.weight} грамм, цвета {orange.color}")
