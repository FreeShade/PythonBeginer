# створить модуль що складається тільки з класу Car


"""Клас моделювання автівки."""  # Docstring - містить стислий опис модуля.


class Car:
    """Знову модулюємо автівку."""

    def __init__(self, make, model, year):
        """Ініціалізувати атрибути, що описують машину."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Повернути відформатоване змістовне ім'я."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Вивести повідомлення з пробігом машини."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Встановити значення одометра.
        Відкинути зміни, якщо йдеться про відмотування одометра.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can`t roll back an odometer!")

    def increment_odometer(self, miles):
        """Додати задане значення до показника одометра."""
        self.odometer_reading += miles


class ElectricCar(Car):
    """Змоделювати властивості, притаманні електрокарам."""

    def __init__(self, make, model, year):
        """
        Ініціалізувати атрибути батьківського класу.
        Після ініціалізувати атрибути електрокара.
        """
        super().__init__(make, model, year)
        self.battery = Battery


# class Battery:
#     """Проста спроба змоделювати акумулятор електрокара."""

#     def __init__(self, battery_size=70):
#         """Ініціалізувати атрибут акумулятора."""
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """Вивести повідомлення про розмір акумулятора."""
#         print(f"This car has a {self.battery_size} - kWh battery.")

#     def get_range(self):
#         """
#         Вивести повідомлення про відстань,
#         яку може подолати авто
#         відповідно до ємності акумулятора.
#         """
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315


#         print(f"This car can go about {range} miles on full charge.")
class Battery:
    """Проста спроба змоделювати акумулятор електрокара."""

    def __init__(self, battery_size=70):
        """Ініціалізувати атрибут акумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Вивести повідомлення про розмір акумулятора."""
        print(f"This car has a {self.battery_size} - kWh battery.")

    def get_range(self):
        """
        Вивести повідомлення про відстань,
        яку може подолати авто
        відповідно до ємності акумулятора.
        """
        if self.battery_size == 70:
            range_miles = 260
        elif self.battery_size == 100:
            range_miles = 315

        print(f"This car can go about {range_miles} miles on full charge.")
