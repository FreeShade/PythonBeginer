# favorite places створіть такий словник, 3 імені будуть ключами , в кожному від 1 до 3 місць

favorite_places = {
    "alex": ["usa", "ukraine", "japan"],
    "mira": ["france", "ukraine", "usa"],
    "luba": ["deught", "usa", "england"],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}`s favorite places are :")
    for place in places:
        if place == "usa":
            print(f"\t{place.upper()}")
        elif place is not "usa":
            print(f"\t{place.title()}")
