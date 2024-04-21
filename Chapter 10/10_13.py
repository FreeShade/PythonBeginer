import json


def get_stored_username():
    """Видобути збережене ім'я, якщо таке є."""
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Запитати ім'я користувача."""
    username = input("What is your name? ")
    filename = "username.json"
    with open(filename, "w") as f:
        json.dump(username, f)
    return username


def greet_user():
    """Привітати користувача на ім'я"""
    username = get_stored_username()
    if username:
        its_you = input(f"Are you {username.title()}? n\y ")
        if its_you == "y":
            print(f"Welcome back, {username.title()}!")
        else:
            username = get_new_username()
            print(f"We`ll remember you when you come back, {username.title()}!")
    else:
        username = get_new_username()
        print(f"We`ll remember you when you come back, {username.title()}!")


greet_user()
