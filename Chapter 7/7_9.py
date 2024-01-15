sandwich_orders = [
    "Bratwurst",
    "Pastrami",
    "Chicken",
    "Reuben",
    "Tuna",
    "Pastrami",
    "Bacon",
    "Pastrami",
    "Pastrami",
    "Meatloaf",
    "Grilled cheese",
    "Pastrami",
]

# Видалити Pastrami сендвічі зі списку замовлень. Списком while.


print("Sorry. We dont have Pastrami sandwiches.")


while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

print(sandwich_orders)
