# збережи обидві програми та оцінити що вийде

import json


def get_stored_f_num():
    """Видобути збережене улюблене число, якщо таке є."""
    filename = "fnumber.json"
    try:
        with open(filename) as f:
            favorite_num = json.load(f)
    except FileNotFoundError:
        favorite_num = input("What is your favorite number? ")
        with open(filename, "w") as f:
            json.dump(favorite_num, f)
            print(f"We`ll remember your favorite number` {favorite_num}")
    else:
        print(f"I know your favorite number is {favorite_num}")


get_stored_f_num()
