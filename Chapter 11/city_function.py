# Місто країна населення


def misto_land(city, country, poppulation=""):
    """Робить назву міста і клаїни стрінгом."""
    if poppulation:
        city_land = f"{city}, {country}, {poppulation}"
    else:
        city_land = f"{city}, {country}"
    return city_land.title()
