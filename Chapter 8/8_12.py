# Бутерброд
# тренування *args


def burger(*toppings):
    """Функція збирає додатки в бутерброд і виводить список"""
    print(toppings)


burger("mushroom")
burger("extra cheese", "tomatos", "fried potato", "salad")
burger("mushroom", "extra cheese", "tomatos", "fried potato", "salad")
