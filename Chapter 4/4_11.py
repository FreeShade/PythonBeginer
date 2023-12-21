# Слайс списку з піцами і виводом через цикл 'for'

pizzas = ["pepperoni", "margarita", "hawaian", "cheese"]

friend_pizzas = pizzas[:]

pizzas.append("sea pizza")
friend_pizzas.append("pork pizza")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("Friend`s favoreti pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())

# for friend_pizza in friend_pizzas:
#    print(f"I like {friend_pizza} pizza.")


# print("I realy love pizza!")
