# Використання quit щоб вийти з циклу
promt = "\nAdd something in your pizza: "
promt += "\nEnter 'quit' for exit. "


while True:
    ingredient = input(promt)

    if ingredient == "quit":
        break
    else:
        print(f"A {ingredient} is add to your pizza.")


# ---------------------------------------------------------------------------------------------------
active_status = True
# Перевірка в операторі while
# Тут же застосована змінна актів
while active_status == True:
    customer_age = input("Please tell your age: ")
    # Використання quit щоб вийти з циклу
    if customer_age == "quit":
        active_status = False

    else:
        customer_age = int(customer_age)

        if customer_age < 3:
            tiket_price = 0
            print(f"Your tiket cost will be {tiket_price} $.")

        elif customer_age >= 3 and customer_age < 12:
            tiket_price = 10
            print(f"Your tiket cost will be {tiket_price} $.")

        elif customer_age >= 12:
            tiket_price = 15
            print(f"Your tiket cost will be {tiket_price} $.")
# ---------------------------------------------------------------------------------------------------

promt = "\nAdd something in your bag : "
promt += "\nEnter 'quit' for exit. "


while True:
    ingredient = input(promt)

    if ingredient == "quit":
        break
    else:
        print(f"A {ingredient} is add to your bag.")
