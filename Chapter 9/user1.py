class User:
    """Моделюємо користувача"""

    def __init__(self, first_name, last_name, age, location, gender):
        """Ініцібвати атрибути користувача."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.gender = gender

    def describe_user(self):
        """Описує користувача"""
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"\nUser`s name is {full_name}")
        print(
            f"{self.gender.title()} is {self.age} years old and live in {self.location.title()}."
        )

    def greet_user(self):
        """Вітає користувача"""
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"Greetings, {full_name}.")
