# Є різні категорії квитків в кіно, залежно від віку
# Питаємо вік
active_status = True

# Напишемо if-else для квитків і цін
# огорнемо це все циклом while
while active_status:
    customer_age = input("Please tell your age: ")

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

# тепер працює як я хотів
