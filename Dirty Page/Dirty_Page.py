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

alien_0 = {"color": "green", "points": 5}
print(alien_0)

del alien_0["points"]
print(alien_0)
