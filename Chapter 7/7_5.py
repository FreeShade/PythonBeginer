# Є різні категорії квитків в кіно, залежно від віку
# Питаємо вік

customer_age = input("Please tell your age: ")
customer_age = int(customer_age)

# Напишемо if-else для квитків і цін

if customer_age < 3:
    tiket_price = 0
elif customer_age >= 3 and customer_age < 12:
    tiket_price = 10
elif customer_age >= 12:
    tiket_price = 15

print(f"Your tiket cost will be {tiket_price} $.")
