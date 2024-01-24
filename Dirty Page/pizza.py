def make_pizza(size, *toppings):
    """Описати піццу яку ми збираємося готувати."""
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f" - {topping}")
