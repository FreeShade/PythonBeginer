cars = ["audi", "bmw", "mercedes", "subaru", "toyota"]


# if car in cars:
#    print(f"{car.title()}, you can chose this car.")

# print(cars == "audi" and cars == "bmw")


for car in cars:
    if car == "bmw" or car == "subaru":
        print(f"{car.title()}, you can drive it.")
print("bmw" in cars)
print("honda" in cars)
