# Mista , напишіть функцію describe_city(), що приймає параметр назву міста та країни,  в
# якій воно розташоване.


def describe_city(city, country="ukraine"):
    print(f"\n{city.title()} is in {country.title()}.")


describe_city("kyiv")
describe_city("krakov", "poland")
describe_city("london", "unated kingdom")
