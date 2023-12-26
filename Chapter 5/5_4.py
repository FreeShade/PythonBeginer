# Продовження минулої вправи вже з if-else конструкцією

alien_color = ["green", "yellow", "red"]
score = 0
player = "Zac"

# Варіант через else

# if "green" in alien_color:
#     score += 5
#     print(f"{player} , you got 5 points.")
# else:
#     score += 10
#     print(f"{player}, you got 10 points.")

# Варіант через 2 if

if "green" in alien_color:
    score += 5
    print(f"{player} , you got 5 points.")
if "green" not in alien_color:
    score += 10
    print(f"{player}, you gor 10 points")


# Добре що це зрозуміло, шкода що немає програми перевірки, можливо напишу щось подібне пізніше
