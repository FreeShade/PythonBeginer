# Продовження минулої вправи вже з if-elif-else конструкцією

alien_color = ["green", "yellow", "red"]
score = 0
player = "Zac"

# Варіант через else

if "green" in alien_color:
    score += 5
    print(f"{player} , you got 5 points.")
elif "yellow" in alien_color:
    score += 10
    print(f"{player} , you got 10 points.")
elif "red" in alien_color:
    score += 15
    print(f"{player} , you got 15 points.")
else:
    score += 10
    print(f"{player}, you got 10 points.")

# Прибираючи із списку інші кольори, я впевнився що всі повідомлення виводяться коректно.
# Вважаю що завдання зроблене коректно.
