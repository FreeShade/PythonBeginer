# Почніть з коду вправи 8_7. напишіть цикл while, де ви будете просити еористувачів ввести ім'я
# музиканта та назву альбому, щойно отримаєте цю інформацію, викличте make_album() на базі
# користувацького вводу та виведить створений словник. Не забудьте додати вихід з циклу...


def make_album(musician_name, album_name):
    """Повернути словник з інформацією про альбом."""
    album_info = f"{musician_name} {album_name}"
    return album_info.title()


# def make_album(musician_name, album_name):
#     """Return a dictionary with information about an album."""
#     album_info = {"musician_name": musician_name, "album_name": album_name}
#     return album_info
# Its wariant of chat GPT code above, at least I`ll whrite all code by myself

while True:
    print("\nPlease tell me musician name: ")
    print("(enter 'q' at any time to quit)")

    musician_name = input("Musician name: ")
    if musician_name == "q":
        break

    album_name = input("Album name: ")
    if album_name == "q":
        break

    formatted_info = make_album(musician_name, album_name)
    print(f"\nHello, {formatted_info}!")


# But if you prefer to return a formatted string, your current implementation is perfectly fine!
# It depends on how you want to structure your program and what kind of data you want to work with.
