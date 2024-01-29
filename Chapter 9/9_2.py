# Візьміть код з 9_1 і створіть кілька екземплярів


# Створить клас Ресторан , створіть екземпляр, викличте по черзі всі методи
class Restaraunt:
    """Моделюємо ресторан"""

    def __init__(self, restaraunt_name, cuisine_type):
        """Ініцібвати атрибути назва та тип кухні."""
        self.restaraunt_name = restaraunt_name
        self.cuisine_type = cuisine_type

    def describe_restaraunt(self):
        """Описує ресторан"""
        print(f"\nA Restaraunt name is {self.restaraunt_name}.")
        print(f"THe restaraunt cuisine is {self.cuisine_type}.")

    def open_restaraunt(self):
        """Повідомляє що заклад працює"""
        print(f"{self.restaraunt_name.title()} is open now.")


# три різні екземпляри класу
rest_0 = Restaraunt("mc`donalds", "american")
rest_1 = Restaraunt("sushi ya", "japanesse")
rest_2 = Restaraunt("yu han ja", "chinese")
rest_3 = Restaraunt("puzata hkhata", "ukrainian")

# Виклик методів
rest_0.describe_restaraunt()
rest_0.open_restaraunt()

rest_1.describe_restaraunt()
rest_1.open_restaraunt()

rest_2.describe_restaraunt()
rest_2.open_restaraunt()

rest_3.describe_restaraunt()
rest_3.open_restaraunt()
