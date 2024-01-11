# Задачка, попросіть користувача загадати число а потім сказати чи кретне воно 10.

some_number = input("Put some number: ")
some_number = int(some_number)

if some_number % 10 == 0:
    print("Ваше число дкратне десяти.")
else:
    print("Here can be your fall.")
