# створити словник за містами, країну розташування, цікавий факт, і тд.

cities = {
    "kyiv": {
        "country": "ukraine",
        "population": "2 952 301 ",
        "fact": 'Kiev known to Russians as the "mother of Russian cities".',
    },
    "london": {
        "country": "unaited kingdom",
        "population": "8 799 728",
        "fact": "London was once the capital of 6 countries at the same time.",
    },
    "tokio": {
        "country": "japan",
        "population": "13 185 502",
        "fact": "Tokyo was called Edo for a very long time",
    },
    "Washington": {
        "country": "Unaited States of America",
        "population": "some people",
        "fact": "Have same name with state Washington",
    },
    "Lviv": {
        "country": "ukraine",
        "population": "some people",
        "fact": "City of Lion.",
    },
}

for city, city_info in cities.items():
    print(f"{city.title()}:")
    for city_in, value in city_info.items():
        print(f"\t{city_in.title()} : {value.title()}")


# print(cities)
