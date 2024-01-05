people = {
    "alex": {
        "first_name": "alex",
        "last_name": "liberty",
        "age": "33",
        "city": "night_city",
    },
    "mira": {
        "first_name": "miroslava",
        "last_name": "liberty",
        "age": "30",
        "city": "night_city",
    },
    "dobby": {
        "first_name": "dobby",
        "last_name": "liberty",
        "age": "405",
        "city": "free",
    },
}

for username, user_info in people.items():
    print(f"\nUsername : {username.title()}")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    location = user_info["city"]

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
