rivers = {
    "nile": "egypt",
    "ukraine": "dnipro",
    "brazil": "amazone",
}
# вивести інформацію про річки
for land, river in rivers.items():
    print(f"The {river.title()} runs through {land.title()}")
# вивести країни
for land in rivers:
    print(land.title())
# вивести річки
for river in rivers.values():
    print(river.title())
