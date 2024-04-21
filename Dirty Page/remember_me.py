# # import json

# # username = input('What is your name ? ')

# # filename = 'username.json'
# # with open(filename, 'w') as f:
# #     json.dump(username, f)
# #     print(f"We'll remembr you when you com back, {username}!")


# import json


# def get_stored_username():
#     """Видобути збережене ім'я, якщо таке є."""
#     filename = "username.json"
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username


# # Рефакторинг
# def greet_user():
#     """Привітати користувача на ім'я"""
#     username = get_stored_username()
#     if username:
#         print(f"Welcome back, {username}!")
#     else:
#         username = input("What is your name? ")
#         filename = "username.json"
#         with open(filename, "w") as f:
#             json.dump(username, f)
#             print(f"We'll remembr you when you com back, {username}!")


# greet_user()
