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
