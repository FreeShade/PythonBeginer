# придумати людей і вилати їм улюблені числа 2.0

favorite_numbers = {
    "alex": [9, 12, 4],
    "holly": [13, 22, 43, 77, 33],
    "samuel": [6, 26],
    "daniel": [3, 2],
    "marta": [1, 3, 7, 67],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}`s favorite number are:")
    for number in numbers:
        print(f"\t{number}")
