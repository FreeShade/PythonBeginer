# Напишіть функцію city_country(), що приймає назву міста і повертає рядрк, відформатований :
# "Santiago, Chile"


def city_country(city, country):
    """Приймає міста і країну і вивдить назви країни і міста."""
    get_city_country = f"{city}, {country}"
    return get_city_country.title()


inputed_info = city_country("kyiv", "ukraine")
print(inputed_info)

inputed_info = city_country("london", "united kingdom")
print(inputed_info)

inputed_info = city_country("tokio", "japan")
print(inputed_info)
