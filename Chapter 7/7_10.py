# Напишіть програму, що питатиму користувача про подорож їхньої мрії.

# user_responses = {}
# polling_active = True
# while polling_active:
#     user = input("\nWhat is your name? ")
#     user_response = input("Which place would you like to travel someday ? ")
#     # Зберегти відповідь у словник
#     user_responses[user] = user_response

#     # Дізнатись чи ще хтось буде проходити опитування.
#     repeat = input("Would you like to let another persone respond? (yes/no) ")

#     if repeat == "no":
#         polling_active = False

# print("\n ---- Poll Results ----")
# for user, user_response in user_responses.items():
#     print(f"{user.title()} would like to travel to {user_response.title()}.")


# Функції , все стає складніше , я вже бувало продовбувався з ними, дуже складно, але ефективно


# def greet_user():
#     """Показати просте вітання."""
#     print("Hello!")

# greet_user()


def greet_user(user_name):
    """Показати просте вітання."""
    print(f"Hello, {user_name.title()}!")


greet_user(input("Something: "))
