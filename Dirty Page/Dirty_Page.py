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

message = input("Tell me something, and I will repeat it back to you: ")
print(message)
