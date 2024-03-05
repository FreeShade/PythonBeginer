# напишіть цикл while, в якому користувачів питають ім'я, і чому їм довподоби програмування

active = True

while active:
    """Записує щoсь кудись, і це важливо."""
    guest_name = input("Please input your name: \nInput 'quit' for end.")

    if guest_name == "quit":
        active = False
        break

    prog = input("Why do you like programing? ")

    print(f"Hello {guest_name.title()}")
    print(f"{prog}")

    file_path = "Chapter 10\guest_book.txt"

    with open(file_path, "a") as guest_file:
        guest_file.write(f"\n{guest_name.title()}\n{prog}\n")
