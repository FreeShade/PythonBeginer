promt = "\nAdd something in your pizza: "
promt += "\nEnter 'quit' for exit. "


while True:
    ingredient = input(promt)

    if ingredient == "quit":
        break
    else:
        print(f"A {ingredient} is add to your pizza.")
