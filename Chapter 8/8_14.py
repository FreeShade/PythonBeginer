# Автівки
def make_car(mark, type, **another_info):
    """Функція зберігає інформацію про авто в словник і повертає його,
    є 2 стабільні аргументи і можливість внести **kwargs"""
    another_info["mark"] = mark
    another_info["type"] = type
    return another_info


car = make_car("subaru", "outback", colo="blue", tow_package=True)

print(car)
