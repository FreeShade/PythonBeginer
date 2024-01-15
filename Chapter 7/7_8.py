sandwich_orders = [
    "Bratwurst",
    "Chicken",
    "Reuben",
    "Tuna",
    "Bacon",
    "Meatloaf",
    "Grilled cheese",
]
finished_sandwiches = []


while sandwich_orders:
    finished_sandwiche = sandwich_orders.pop()
    print(f"\n I was make your {finished_sandwiche} for you.")
    finished_sandwiches.append(finished_sandwiche)


print("\nAll sandwiches are ready.")
print(finished_sandwiches)
