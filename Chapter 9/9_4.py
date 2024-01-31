# Почніть з коду 9_1
# Створить клас Ресторан , створіть екземпляр, викличте по черзі всі методи
class Restaraunt:
    """Моделюємо ресторан"""

    def __init__(self, restaraunt_name, cuisine_type):
        """Ініцібвати атрибути назва та тип кухні."""
        self.restaraunt_name = restaraunt_name
        self.cuisine_type = cuisine_type
        self.number_serve = 0

    def describe_restaraunt(self):
        """Описує ресторан"""
        print(f"A Restaraunt name is {self.restaraunt_name}.")
        print(f"THe restaraunt cuisine is {self.cuisine_type}.")

    def open_restaraunt(self):
        """Повідомляє що заклад працює"""
        print(f"{self.restaraunt_name.title()} is open now.")

    def set_number_severed(self):
        """Встановлює кількість клієнтів і виводить його."""
        print(f"There are : {self.number_serve} clients.")

    def incrment_number_severed(self, clients):
        """Дозволяє змінити кількість клієгтів."""
        self.number_serve += clients


# Екземпляр класу
rest = Restaraunt("mc`donalds", "american")
# Виклик методів
rest.describe_restaraunt()
rest.open_restaraunt()

rest.number_serve = 2
rest.set_number_severed()

rest.incrment_number_severed(23)
rest.set_number_severed()


rest.incrment_number_severed(-3)
rest.set_number_severed()
