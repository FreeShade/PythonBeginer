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


# Admin can: 'ban user', 'can add post',
class Admin(User):
    """
    Особливий користувач , може банити, постити, видаляти
    """

    def __init__(self, first_name, last_name, age, location, gender):
        super().__init__(first_name, last_name, age, location, gender)
        self.privileges = privileges


class Privileges(Admin):
    """Моделюємо привілегії."""

    def show_privileges(self):
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"{full_name} can: {privileges}")


privileges = ["can add post", "can delete post", "can ban user"]
user_0 = User("oleksander", "pustovoi", 32, "ukraine", "he")
user_1 = User("miroslava", "pustova", 30, "ukraine", "shee")
user_2 = User("takeuchi", "miamoto", 67, "japan", "he")
admin_user = Privileges("axel", "suter", 77, "haven", "he")
