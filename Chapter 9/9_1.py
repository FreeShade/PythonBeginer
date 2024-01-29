# Створить клас Ресторан , створіть екземпляр, викличте по черзі всі методи


class Restaraunt:
    """Моделюємо ресторан"""

    def __init__(self, restaraunt_name, cuisine_type):
        """Ініцібвати атрибути назва та тип кухні."""
        self.restaraunt_name = restaraunt_name
        self.cuisine_type = cuisine_type

    def describe_restaraunt(self):
        """Описує ресторан"""
        print(f"A Restaraunt name is {self.restaraunt_name}.")
        print(f"THe restaraunt cuisine is {self.cuisine_type}.")

    def open_restaraunt(self):
        """Повідомляє що заклад працює"""
        print(f"{self.restaraunt_name.title()} is open now.")


# Екземпляр класу
rest = Restaraunt("mc`donalds", "american")
# Виклик методів
rest.describe_restaraunt()
rest.open_restaraunt()