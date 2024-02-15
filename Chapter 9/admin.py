from user1 import User


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
