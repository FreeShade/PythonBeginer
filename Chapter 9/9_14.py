# Лотерея
from random import choice

sight_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "s", "d", "f", "g"]


def make_tiket():
    tiket = []
    """Створює квиток."""
    for sight in range(4):
        chose = choice(sight_list)
        tiket.append(chose)
    return tiket


tiket = make_tiket()
print(tiket)
