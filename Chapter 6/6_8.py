# Створить кілька словників і вставте туди інформацію про тваринок


pets = []
# print(pets)
pet_info_1 = {
    "owner": "alex",
    "name": "yumi",
    "pet": "cat",
    "age": "6",
}
pet_info_2 = {
    "owner": "mira",
    "name": "miko",
    "pet": "dog",
    "age": "3",
}

for pet_info, value in pet_info_1.items():
    print(f"{pet_info.title()} : {value}")
pets.append(pet_info_1)

print("\n")

for pet_info, value in pet_info_2.items():
    print(f"{pet_info.title()} : {value.title()}")
pets.append(pet_info_2)


# print(pets)
