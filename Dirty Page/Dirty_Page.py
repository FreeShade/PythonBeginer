# players = ["charles", "martina", " michael", "florence", "eli"]
# print(players[0:3])
# print(players[1:4])
# print(players[:4])
# print(players[2:])
# print(players[-3:])


# players = ["charles", "martina", "michael", "florence", "eli"]
# print("Here are the first three players on my team:")
# for player in players[:3]:
#    print(player.title())


# my_foods = ["pizza", "falafel", "carrot cake"]
# friend_foods = my_foods[:]

# my_foods.append("cannoli")
# friend_foods.append("ice ceam")


# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend`s favorite foods are:")
# print(friend_foods)


# Tuples Кортежі , не любив їх і не люблю.


# for i in range(30):
#    i += 1
#    print("*" * i)
# input()

# --------------------------------------------------------------------------------------------------
# П'ятий розділ , боротьба з 'if' думаю в цей раз буде простіше.
# --------------------------------------------------------------------------------------------------

# cars = ["audi", "bmw", "subaru", "toyota"]

# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     else:
#         print(car.title())

# car = "bmw"
# print(car == "bmw")

# car = "audi"
# print(car == "bmw")


# car = "bmw"
# print(car == "audi")


# car = "Audi"
# print(car.lower() == "audi")


# requested_topping = "mushrooms"

# if requested_topping != "anchovies":
#     print("Hold the anchovies !")


# age = 18
# print(age == 18)


# answer = 17

# if answer != 42:
#     print("That is not the correct answer. please try again!")


# age = 19
# print(age < 21)
# print(age <= 21)
# print(age > 21)
# print(age >= 21)


# age_0 = 22
# age_1 = 18
# print(age_0 >= 21 and age_1 >= 21)

# age_1 = 22

# print(age_0 >= 21 and age_1 >= 21)


# age_0 = 22
# age_1 = 18
# print(age_0 >= 21 or age_1 >= 21)

# requested_toppings = ["mushrooms", "onions", "pineapple"]
# print("mushrooms" in requested_toppings)
# print("peperoni" in requested_toppings)


# banned_users = ["andrew", "carolina", "david"]
# user = "marie"
# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish.")


# game_active = True
# cant_edit = False


# if conditional_test:
#     do something

# age = 17

# if age >= 18:
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")
# else:
#     print("Sorry, you are too young to vote.")
#     print("Please register to vote as soon as you turn 18!")

# age = 12

# if age < 4:
#     print("your admission cost is $0.")
# elif age < 18:
#     print("Your admission cost is $25")
# else:
#     print("Your admission cost is $40.")


# age = 12

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# else:
#     price = 40

# print(f"You admission cost is ${price}")


# age = 12

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# else:
#     price = 20

# print(f"Your admission cost is ${price}.")

# age = 12

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# elif age >= 65:
#     price = 20

# # print(f"Your admission cost is ${price}.")


# requested_toppings = ["mushrooms", "extra cheese"]

# if "mushrooms" in requested_toppings:
#     print("Adding mushrooms.")
# if "pepperoni" in requested_toppings:
#     print("Adding pepperoni.")
# if "extra cheese" in requested_toppings:
#     print("Adding extra cheese.")

# print("\nFinished making your pizza.")


# Використання if у поєднанні зі списками


# requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

# for requested_topping in requested_toppings:
#     print(f"Adding {requested_topping}.")
# print("\nFinished making your pizza!")


# requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

# for requested_topping in requested_toppings:
#     if requested_topping == "green peppers":
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Adding {requested_topping}.")

# print("\nFinished making your pizza!")


# requested_toppings = []

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")


# Step 1  визначаємо список доступних інгредієнтів
# available_toppings = [
#     "mushrooms",
#     "olives",
#     "green peppers",
#     "pepperoni",
#     "pineapple",
#     "extra cheese",
# ]
# # Step 2 список замовлених інгредієгтів
# requested_toppings = ["mushrooms", "french fries", "extra cheese"]
# # Step 3 проходимо по спуску, якщо є то додаємо , якщо немає то виводимо else
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping}.")
#     else:
#         print(f"Sorry, we don`t have {requested_topping}.")

# print("\nFinished making your pizza.")


# Dictionary. hard for me too

# alien_0 = {"color": "green", "points": 5}

# print(alien_0["color"])
# print(alien_0["points"])


# alien_0 = {"color": "green"}
# print(alien_0["color"])


# alien_0 = {"color": "green", "points": 5}

# new_points = alien_0["points"]
# print(f"You just earned {new_points} points !")

# PAGE 1 HUNDRED !!!! Congradulation !!!!!!!!

# alien_0 = {"color": "green", "points": 5}
# print(alien_0)

# alien_0["x_position"] = 0
# alien_0["y_position"] = 25

# print(alien_0)


# alien_0 = {}

# alien_0["color"] = "green"
# alien_0["points"] = 5

# print(alien_0)


# alien_0 = {"color": "green"}
# print(f"The alien is {alien_0['color']}")

# alien_0["color"] = "yelow"
# print(f"the alien is now {alien_0['color']}")


# alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
# print(f"Original position: {alien_0['x_position']}")

# # Зсунути прибульця праворуч.
# # Визначити, як далеко зсунути прибульця,
# # зважаючи на його поточну швидкість.

# if alien_0["speed"] == "slow":
#     x_increment = 1
# elif alien_0["speed"] == "medium":
#     x_increment = 2
# else:
#     # Це швидкий прибулець
#     x_increment = 3

# # Нове розташування - - це старе розташування плюс зміщення.
# alien_0["x_position"] = alien_0["x_position"] + x_increment

# print(f"New position: {alien_0['x_position']}")

# alien_0 = {"color": "green", "points": 5}
# print(alien_0)

# del alien_0["points"]
# print(alien_0)

# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edvard": "ruby",
#     "phil": "python",
# }

# language = favorite_languages["sarah"].title()
# print(f"Sarah`s favorite language is {language}.")


# alien_0 = {
#     "color": "green",
#     "speed": "slow",
# }
# point_value = alien_0.get("points", "No point value assigned.")
# print(point_value)


# Cycle over dictionary


# user_0 = {
#     "username": "efermi",
#     "first": "enrico",
#     "last": "fermi",
# }

# for key, value in user_0.items():
#     print(f"\nKey : {key}")
#     print(f"Value : {value}")


# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "ruby",
#     "phil": "python",
# }

# for name, language in favorite_languages.items():
#     print(f"\n{name.title()}`s favorite language is {language.title()}.")


# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "ruby",
#     "phil": "python",
# }

# Перебір ключів в словнику.
# for name in favorite_language: нічим не відрізняється
# for name in favorite_languages.keys():
#    print(name.title())


# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "ruby",
#     "phil": "python",
# }

# friends = ["phil", "sarah"]
# for name in favorite_languages:
#     print(f"Hi {name.title()}")

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I soo you love {language}!")


# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "ruby",
#     "phil": "python",
# }

# if "erin" not in favorite_languages:
#     print("Erin, please take our poll!")


# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "ruby",
#     "phil": "python",
# }
# Відсортувати ключі , зручно і перспективно.

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "ruby",
#     "phil": "python",
# }

# print("The following languages have been mentioned: ")
# for language in favorite_languages.values():
#     print(language.title())


# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "ruby",
#     "phil": "python",
# }
# #використання set щоб прибрати повторювані пункти.
# print("The following languages have been mentioned: ")
# for language in set(favorite_languages.values()):
#     print(language.title())

# Множини
# languages = {"python", "ruby", "python", "c"}
# print(languages)


# Вкладання в пітон(і)

# alien_0 = {"color": "green", "points": 5}
# alien_1 = {"color": "yelow", "points": 10}
# alien_2 = {"color": "red", "points": 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# Створимо флот прибульців:

# # створити порожній список
# aliens = []

# # Cтворити 30 зелених прибульців.
# for alien_number in range(30):
#     new_alien = {"color": "green", "points": 5, "speed": "slow"}
#     aliens.append(new_alien)

# # показати перших 5 прибульців.

# for alien in aliens[:5]:
#     print(alien)
# print("...")

# # Показати, скільки прибульців створено.
# print(f"Total number of aliens: {len(aliens)}")


# # створити порожній список
# aliens = []

# # Cтворити 30 зелених прибульців.
# for alien_number in range(30):
#     new_alien = {"color": "green", "points": 5, "speed": "slow"}
#     aliens.append(new_alien)

# for alien in aliens[:3]:
#     if alien["color"] == "green":
#         alien["color"] = "yelow"
#         alien["speed"] = "medium"
#         alien["points"] = 10
#     elif alien["color"] == "yelow":
#         alien["color"] = "red"
#         alien["speed"] = "fast"
#         alien["points"] = 15
# # показати перших 5 прибульців.

# for alien in aliens[:3]:
#     print(alien)
# print("...")


# Зберегти інформацію про замовлення

# pizza = {"crust": "thick", "toppings": ["mushrooms", "extra cheese"]}

# # Підсумувати замовлення
# print(f"You ordered a {pizza['crust']} - crust pizza." "with the following topings: ")
# for topping in pizza["toppings"]:
#     print("\t" + topping.title())


# favorite_languages = {
#     "jen": ["python", "ruby"],
#     "sarah": ["c"],
#     "edward": ["ruby", "go"],
#     "phil": ["python", "haskell"],
# }

# for name, languages in favorite_languages.items():
#     print(f"\n{name.title()}`s favorite language are:")
#     for language in languages:
#         print(f"\t{language.title()}")

# users = {
#     "aeinstein": {
#         "first": "albert",
#         "last": "einstein",
#         "location": "princeton",
#     },
#     "mcurie": {
#         "first": "marie",
#         "last": "curie",
#         "location": "paris",
#     },
# }

# for username, user_info in users.items():
#     print(f"\nUsername: {username}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info["location"]

#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")


# Ну що ж , в мене краще зі словниками, тепер хоч розумію як їх ітерувати в циклі, плюсик в карму.
# Далі ввід і цикл while... Безкінечність не межа.

# input() функція ставить програму на пауху і чекає , доки користувач введе якийсь текст. Приклад:

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)


# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")


# promt = "If you tell us who are, we can personalize the messages you see."
# promt += "\nWhat is your first name ? "

# name = input(promt)

# print(f"\nHello, {name} !")

# age = input("How old are you? ")
# print(type(age))


# age = input("How old are you? ")
# age >= 18
# print(age)


# age = input("How old are you? ")

# age = int(age)
# age >= 18
# print(type(age))


# height = input("How tall are you, in inches? ")
# height = int(height)

# if height >= 48:
#     print("\nYou're tall enough to ride !\n")
# else:
#     print("\n-------------------------------------------------")
#     print("You'll be able to ride when you're a little older.")
#     print("-------------------------------------------------\n")


# Оператор остачі

# number = input("Enter a number, and I`ll tell you if it`s even or odd: ")
# number = int(number)

# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")


# Далі цикл while.

# curent_number = 1

# while curent_number <= 5:
#     print(curent_number)
#     curent_number += 1


# promt = "\nTell me something, and I will repeat it back to you: "
# promt += "\nEnter 'quit' to end the program. "
# message = None
# while True:
#     if message == "quit":
#         print("Bye!")
#         break
#     else:
#         message = input(promt)
#         print(message)
#

# promt = "\nTell me something, and I will repeat it back to you: "
# promt += "\nEnter 'quit' to end the program. "

# message = None

# while message != "quit":
#     message = input(promt)

#     if message != "quit":
#         print(message)


# promt = "\nTell me something, and I will repeat it back to you: "
# promt += "\nEnter 'quit' to end the program. "

# active = True
# while active:
#     message = input(promt)

#     if message == "quit":
#         active = False

#     else:
#         print(message)


# promt = "\nTell me something, and I will repeat it back to you: "
# promt += "\nEnter 'quit' to end the program. "


# while True:
#     city = input(promt)

#     if city == "quit":
#         break
#     else:
#         print(f"I`d like to go to {city.title()}")


# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue

#     print(current_number)


# Нескінченні цикли :

# x = 1
# while x <= 5:
#     print(x)


# Цикл while і словники та списки
# # Почати з користувачів, яких треба перевірити,
# # та порожнього списку підтверджених користувачів.
# unconfirmed_users = ["alice", "brian", "candace"]
# confirmed_users = []

# # Перевіряти кожного користувача, доки непідтверджені користувачі не закінчаться.
# # Переносити кожного перевіреного користувача до списку підтверджених користувачів.
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user : {current_user.title()}")
#     confirmed_users.append(current_user)

# # Показати всіх підтверджених користувачів
# print("\nThe following users have been confirmed: ")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# # remove зі списку, циклом while

# pets = ["dog", "cat", "goldfish", "cat", "rebbit", "cat"]
# print(pets)

# while "cat" in pets:
#     pets.remove("cat")

# print(pets)


# responses = {}

# # Вставити булеву змінну у значення, що показує: опитування в процесі.

# polling_active = True

# while polling_active:
#     # Спитати ім'я людини та її відповідь.
#     name = input("\nWhat is your name ? ")
#     response = input("Which mountain would you like to climb someday? ")

#     # Зберегти відповідь у словник.
#     responses[name] = response

#     # Дізнатись чи ще хтось буде проходити опитування.
#     repeat = input("Would you like to let another persone respond? (yes/no) ")

#     if repeat == "no":
#         polling_active = False


# # Опитування завершене. Показати результат.
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name.title()} would like to climb {response}.")


# Функції , все стає складніше , я вже бувало продовбувався з ними, дуже складно, але ефективно


# def greet_user():
#     """Показати просте вітання."""
# #     print("Hello!")

# # greet_user()


# def greet_user(user_name):
#     """Показати просте вітання."""
#     print(f"Hello, {user_name.title()}!")


# greet_user(input("Something: "))

# Опитування завершене. Показати результат.
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name.title()} would like to climb {response}.")


# some ne text to chek comits


# def describe_pet(animal_type, pet_name):
#     """Показати інформацію про домашнього улюбленця."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}`s name is {pet_name.title()}.")


# describe_pet("humster", "harry")
# describe_pet("dog", "willie")
# describe_pet(pet_name="yumi", animal_type="cat")


# def describe_pet(pet_name, animal_type="dog"):
#     """Показати інформацію про домашнього улюбленця."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}`s name is {pet_name.title()}.")


# # Both variants are same:
# describe_pet(pet_name="willie")
# describe_pet("willie")

# # no I change animal type in function
# describe_pet(pet_name="Harry", animal_type="cat")


# Щось там далі , не знаю що , але сьогодні коміт апну.
# З почином !
# Значення яке повертає функція


# Функція яка повертає відформатований рядок ім'я прізвище
# def get_formatted_name(first_name, last_name):
#     """Повертатиме відформатоване повне ім'я."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()


# musician = get_formatted_name("jimi", "hendrix")

# print(musician)


# # Розширимо функціонал функції вище
# def get_formatted_name(first_name, middle_name, last_name):
#     """Повернути відформатоване повне ім'я."""
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()


# musician = get_formatted_name("john", "lee", "hooker")
# print(musician)

# Змінимо функцію щоб друге ім'я було не обов'язковим


# def get_formatted_name(first_name, last_name, middle_name=""):
#     """Повернути відформатоване повне ім'я."""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()


# musician = get_formatted_name("jimi", "hendrix")
# print(musician)

# musician = get_formatted_name("john", "hooker", "lee")
# print(musician)


# Повернення словника


# def build_person(first_name, last_name):
#     """Повернути словник з інформацією про людину."""
#     person = {"first": first_name, "last": last_name}
#     return person


# musician = build_person("jimi", "hendrix")
# print(musician)


# def build_person(first_name, last_name, age=None):
#     """Повернути словник з інформацією про людину."""
#     person = {"first": first_name, "last": last_name}
#     if age:
#         person["age"] = age
#     return person


# musician = build_person("jimi", "hendrix", age=27)
# print(musician)


# def get_formatted_name(first_name, last_name, age=None):
#     """Повернути словник з інформацією про людину."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()


# # Це нескінченний циклm
# while True:
#     print("\nPlease tell me your name: ")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name} !")


# def get_formatted_name(first_name, last_name):
#     """Повернути відформатоване повне ім'я"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()


# while True:
#     print("\nPlease tell me your name: ")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == "q":
#         break

#     l_name = input("Last name: ")
#     if l_name == "q":
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")


# Продовження Передавання списку


# def greet_users(names):
#     """Вивести просте повідомлення для кожного користувача у списку."""
#     for name in names:
#         message = f"Hello, {name.title()}!"
#         print(message)


# usernames = ["hennah", "ty", "margot"]
# greet_users(usernames)


# Редагування списку всередині функції

# # Почати з креслень, які треба роздрукувати.
# unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
# completed_models = []

# # Симулювати друк кожного креслення, доки всі не закінчаться.
# # Перенести кожен малюнок до completed_models після друку.
# while unprinted_designs:
#     current_designs = unprinted_designs.pop()
#     print(f"Printing model: {current_designs}")
#     completed_models.append(current_designs)

# # Показати всі готові моделі.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)


# Реорганізація коду вище


# def print_models(unprinted_designs, completed_models):
#     """
#     Симулювати друк кожного креслення, доки всі не закінчаться.
#     Перенести кожен малюнок до completed_models після друку.
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)


# def show_completed_models(completed_models):
#     """Показати всі надруковані моделі."""
#     print("\nThe following models have been printed.")
#     for completed_model in completed_models:
#         print(completed_model)


# unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)


# Як не дозволити функції видозмінити список
# як , як , копіювати замість зміни, список в функції заміни зміну на копію і бек ап залишиться

# Передання довільної кількості аргументів


# def make_pizza(*toppings):
#     """Склісти список замовлених інгредієнтів."""
#     print(toppings)


# make_pizza("pepperoni")
# make_pizza("mushroom", "green pepers", "extra cheese")


# def make_pizza(*toppings):
#     """Описати піцу, яку ми збираємося приготувати."""
#     print("\nMaking a pizza with the following toppings: ")
#     for topping in toppings:
#         print(f" - {topping}")


# make_pizza("pepperoni")
# make_pizza("mushrooms", "green peppers", "extra cheese")

# # додамо параметр розміру піци


# def make_pizza(size, *toppings):
#     """Описати піцу,яку ми збираємося приготувати."""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f" - {topping}")


# make_pizza(16, "pepperoni")
# make_pizza(12, "mushrooms", "green peppers", "extra cheese")


# #*args - параметр збору довільних позиційних аргументів


# Довільні ключові аргументи **kwargs


# def build_profile(first, last, **user_info):
#     """Створити словник, що міститиме всю інформацію про користувача."""
#     user_info["first_name"] = first
#     user_info["last_name"] = last
#     return user_info


# user_profile = build_profile(
#     "albert", "einstein", location="princeton", field="physics"
# )

# print(user_profile)

# **kwargs - набір неописаних ключових аргументів.

# Зберігання функції у модулі, продовжу завтра, або ввечорі.
# імпорт в цій же папці, але іншими файлами.


# Можна імпортувати окремі функції з модуля.
# from module_name import function_name
# або
# from module_name import function_0, function_1, function_2


# Ключове слово as: як дати функції псевдонім


# Далі класи... Пиздець.
# Ну і об'єктно орієнтовне програмування


# # Песик
# class Dog:
#     """Проста спроба змоделювати собаку."""

#     def __init__(self, name, age):
#         """Ініціювати атрибути"""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """Симулювати виконання команди сидіти"""
#         print(f"{self.name} is now sitting.")

#     def roll_over(self):
#         """Cимулювати команду 'лежати'."""
#         print(f"{self.name} rolled over!")


# # Створення екземпляру класу
# my_dog = Dog("Willie", 6)
# # Звернення до атрибутів
# print(f"My dog`s name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years age.")
# # Виклик методів
# my_dog.sit()
# my_dog.roll_over()


# # Створення багатьох екземплярів
# your_dog = Dog("Lucy", 3)


# print(f"\nYour dog`s name is {your_dog.name}")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.sit()


# print("This is a test commit")


# Робота з класами і екземплярами класів


# class Car:
#     """Проста спроба змоделювати машину."""

#     def __init__(self, make, model, year):
#         """Ініціалізувати атрибути, що описують машину."""
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_describptive_name(self):
#         """Повернути відформатоване змістовне ім'я."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()


# my_new_car = Car("audi", "a4", 2019)
# print(my_new_car.get_describptive_name())

# # Уставне значення атребуту
# class Car:
#     """Проста спроба змоделювати машину."""

#     def __init__(self, make, model, year):
#         """Ініціалізувати атрибути, що описують машину."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0  # не обов'язково передавати в ІНІТ .

#     def get_describptive_name(self):
#         """Повернути відформатоване змістовне ім'я."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         """Вивести повідомлення з пробігом машини"""
#         print(f"This car has {self.odometer_reading} miles on it.")


# my_new_car = Car("audi", "a4", 2019)
# print(my_new_car.get_describptive_name())
# my_new_car.read_odometer()


# # Необов1язкова зміна атрибуту
# class Car:
#     """Проста спроба змоделювати машину."""

#     def __init__(self, make, model, year):
#         """Ініціалізувати атрибути, що описують машину."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_describptive_name(self):
#         """Повернути відформатоване змістовне ім'я."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         """Вивести повідомлення з пробігом машини"""
#         print(f"This car has {self.odometer_reading} miles on it.")


# my_new_car = Car("audi", "a4", 2019)
# print(my_new_car.get_describptive_name())

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()


# Зміна значень атрибута в методі
# class Car:
#     """Проста спроба змоделювати машину."""

#     def __init__(self, make, model, year):
#         """Ініціалізувати атрибути, що описують машину."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_describptive_name(self):
#         """Повернути відформатоване змістовне ім'я."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         """Вивести повідомлення з пробігом машини"""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         # """Задати значення одометра."""
#         # self.odometer_reading = mileage
#         # Можна розширити
#         """
#         Задата значення одометра.
#         Відкинути зміну в разі спроби відмотати показники одометра.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can`t roll back an odometer!")


# my_new_car = Car("audi", "a4", 2019)
# print(my_new_car.get_describptive_name())

# my_new_car.update_odometer(24)
# my_new_car.read_odometer()

# my_new_car.update_odometer(23)# тест.
# my_new_car.read_odometer()


# Збільшення атрибута у методі


# class Car:
#     """Проста спроба змоделювати машину."""

#     def __init__(self, make, model, year):
#         """Ініціалізувати атрибути, що описують машину."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_describptive_name(self):
#         """Повернути відформатоване змістовне ім'я."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         """Вивести повідомлення з пробігом машини"""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         """Задати значення одометра."""
#         self.odometer_reading = mileage

#     def increment_odometer(self, miles):
#         """Додати значення до показника одометра."""
#         self.odometer_reading += miles


# my_used_car = Car("subaru", "outback", 2015)
# print(my_used_car.get_describptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()


# # Далі Успадкування класів


# class Car:
#     """Знову модулюємо автівку."""

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can`t roll back an odometer!")

#     def increment_odometer(self, miles):
#         self.odometer_reading += miles


# # Екземпляри як атрибути.
# class Battery:
#     """Проста спроба змоделювати акумулятор електрокара."""

#     def __init__(self, battery_size=75):
#         """Ініціалізувати атрибути акумулятора."""
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """Вивести повідомлення про розмір акумулятора."""
#         print(f"This car has a {self.battery_size} - kWh battery.")

#     def get_range(self):
#         """
#         Вивести повідомлення про відстань,
#         яку можее подолати авто відповідно
#         до ємності акумулятора.
#         """
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315

#         print(f"This car can go about {range} miles on a full charge.")


# class ElectricCar(Car):
#     """Змоделювати властивості, притаманні електрокарам."""

#     # Визначення атрибутів і методів породженого класу.
#     def __init__(self, make, model, year):
#         """Започаткувати атрибути батьківського класу."""
#         super().__init__(make, model, year)
#         # Додаємо атрибут властивий тільки електрокарам.
#         # self.battery_size = 75
#         self.battery = Battery()

#     # def describe_battery(self):
#     #     """Вивести повідомлення про розмір акумулятора."""
#     #     print(f"This car has a {self.battery_size} - kWh battery.")

#     #     # Перевизначення методів батьківського класу

#     def fill_gas_tank(self):
#         """Електрокари не мають бензобаків!"""
#         print("This car dosen`t need a gas tank!")


# my_tesla = ElectricCar("tesla", "model s", 2019)
# print(my_tesla.get_descriptive_name())
# # my_tesla.describe_battery()
# # my_tesla.fill_gas_tank() # Перевірка методу.

# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()


# Імпортування класів.
# Важко було , але справився.


# створить модуль що складається тільки з класу Car
# class Car:
#     """Знову модулюємо автівку."""

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can`t roll back an odometer!")

#     def increment_odometer(self, miles):
#         self.odometer_reading += miles


# Збереження кількох класів в одному модулі (car.py)
# Імпортування багатьлх класів з одного модуля. (my_cars.py)
# Імпорт цілого модуля.

# Імпортування всіх класів з модуля
# from module_name import*


# Імпортування модуля в інший модуль
# (my_car.py) все там.


# Використання псевдонімів
# from electric_car import ElectricCar as EC

# my_tesla = EC("tesla", "roadster", 2019)

# Наступний крок 3 задачки.


# Стандартна бібліотека Python

# from random import randint

# print(randint(1, 6))


# from random import choice

# players = ["charles", "martina", "michael", "florence", "eli"]
# first_up = choice(players)

# print(first_up.title())


# Робота з файлами та вийнятки.

# with open("Dirty Page/pi_d.txt") as file_object:
#     contents = file_object.read()
# print(contents.rstrip())


# # import os


# # os.chdir(r"C:\Users\Natrix\Desktop\repositories\PythonBeginer\Dirty Page")
# # print("Поточний каталог:", os.getcwd())
# # буква "r" в коді нижче допомагає не дублювати "\\" дуже зручно
# file_path = r"C:\Users\Natrix\Desktop\repositories\PythonBeginer\Dirty Page\pi_d.txt"
# with open(file_path) as file_object:
#     contents = file_object.read()
# print(contents)

# Більшість коду буде в інших файліх в цій папці.


# Зчитування рядок за рядком.

# filename = r"Dirty Page\pi_d.txt"

# with open(filename) as file_object:
#     for line in file_object:
#         # print(line)
#         print(line.rstrip())


# Створення списку рядків на базі файлу

# file_name = r"Dirty Page\pi_d.txt"

# with open(file_name) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())

# Робота з вмістом файлу
file_name = r"Dirty Page\pi_d.txt"

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    # pi_string += line.rstrip()
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
