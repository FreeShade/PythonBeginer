# Змініть функцію make_shirt() щоб футболки мали заданий розмір L


def make_shirt(text_on_shirt="I love Python", shirt_size="L"):
    print(f"\nYour shirt`s size is {shirt_size.upper()}.")
    print(f"The text on your shirt is : {text_on_shirt}.")


make_shirt()
make_shirt(shirt_size="M")
make_shirt(text_on_shirt="Some shit", shirt_size="XXXL")
