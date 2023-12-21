# Продовбав в написав вивід в консолі зразу зробив цикли через for і вивів їх окремо
# От такі справи, або я просто не зрозумів завдання, пізніше повернусь і перероблю , якщо зрозумію в чому помилка

pizzas = ["pepperoni", "margarita", "hawaian", "cheese"]

friend_pizzas = pizzas[:]

pizzas.append("sea pizza")
friend_pizzas.append("pork pizza")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("\n")

print("Friend`s favoreti pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())
