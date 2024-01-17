# Напишіть функцію make_shirt() , що приймає параметр розмір футболки та текст на ній.


def make_shirt(shirt_size, text_on_shirt):
    print(f"\nYour shirt`s size is {shirt_size.upper()}.")
    print(f"The text on your shirt is : {text_on_shirt}.")


make_shirt("xxxl", "it`s can be your text")
make_shirt(text_on_shirt="XXXXL", shirt_size="s")
