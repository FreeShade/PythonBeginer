# Додайте атрибут до класу User


# Визначте клас User, дайте йому птрибути
class User:
    """Моделюємо користувача"""

    def __init__(self, first_name, last_name, age, location, gender):
        """Ініцібвати атрибути користувача."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.gender = gender
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """Збільшує спроби авторизації на 1."""
        self.login_attempts += 1
        print(f"There are: {self.login_attempts} logins.")

    def reset_login_attempts(self):
        """Обнуляє кількість авторизацій."""
        self.login_attempts = 0
        print(f"There are: {self.login_attempts} logins.")


# Створюємо екземрляри класу
user_0 = User("oleksander", "pustovoi", 32, "ukraine", "he")
user_1 = User("miroslava", "pustova", 30, "ukraine", "shee")
user_2 = User("takeuchi", "miyamoto", 67, "japan", "he")


# Викликаємо методи екземплярів
user_0.describe_user()
user_0.greet_user()

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.reset_login_attempts()
user_0.increment_login_attempts()


# Викликали спробували, каряво але працює.
