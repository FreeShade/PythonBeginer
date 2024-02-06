# Оновити бетереї, взяти


class Car:
    """Знову модулюємо автівку."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can`t roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# Екземпляри як атрибути.
class Battery:
    """Проста спроба змоделювати акумулятор електрокара."""

    def __init__(self, battery_size=75):
        """Ініціалізувати атрибути акумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Вивести повідомлення про розмір акумулятора."""
        print(f"This car has a {self.battery_size} - kWh battery.")

    def get_range(self):
        """
        Вивести повідомлення про відстань,
        яку можее подолати авто відповідно
        до ємності акумулятора.
        """
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def update_battery(self):
        """
        Моделювання оновлення бетереї.
        """
        # Додав оновлення бетереї. Все спрацювало.
        if self.battery_size <= 100:
            self.battery_size = 100


class ElectricCar(Car):
    """Змоделювати властивості, притаманні електрокарам."""

    # Визначення атрибутів і методів породженого класу.
    def __init__(self, make, model, year):
        """Започаткувати атрибути батьківського класу."""
        super().__init__(make, model, year)
        # Додаємо атрибут властивий тільки електрокарам.
        # self.battery_size = 75
        self.battery = Battery()

    # def describe_battery(self):
    #     """Вивести повідомлення про розмір акумулятора."""
    #     print(f"This car has a {self.battery_size} - kWh battery.")

    #     # Перевизначення методів батьківського класу

    def fill_gas_tank(self):
        """Електрокари не мають бензобаків!"""
        print("This car dosen`t need a gas tank!")


my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
# my_tesla.fill_gas_tank() # Перевірка методу.

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# Додав оновлення бетереї. Все спрацювало.
my_tesla.battery.update_battery()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
