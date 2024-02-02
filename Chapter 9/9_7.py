# Візочок з морозивом.
# Напишіть клас IceCreamStand , що наслідує клас Restaraunt


# Почніть з коду 9_1
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


class IceCreamStand(Restaraunt):
    """
    Наслідує клас Restaraunt,
    моделюємо властивості морозива
    чи чогось подібного.
    """

    def __init__(self, restaraunt_name, cuisine_types, favours):
        super().__init__(restaraunt_name, cuisine_types)
        self.favours = favours
        self.IceCreamStand()

    def IceCreamStand(self):
        """Відображатиме список наповнювачів."""
        print(f"There are a list of favours: {self.favours}")


favours = ["cherry", "vanila", "strawberry", "blackberry"]
# Екземпляр класу
rest = IceCreamStand("Ice World", "Sweets", favours)
rest.IceCreamStand()
rest.describe_restaraunt()


# Все що заявлено виводить, криво , бо легасі код це ще та дрянь
# Спробую в чати GPT перевірити.
# зробив пару незначних помилок
# print(rest.describe_restaraunt())
# rest.IceCreamStand()  # виправлено цей рядок
