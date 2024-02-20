# Lottery analize
from random import choice


sight_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "s", "d", "f", "g"]
my_tiket = ["1", "2", "3", "4"]
active = True
trys = 0


def make_tiket():
    """Створює квиток."""
    tiket = []
    for sight in range(4):
        chose = choice(sight_list)
        tiket.append(chose)
    return tiket


while active:
    tiket = make_tiket()
    print(tiket)
    trys += 1
    if my_tiket != tiket:
        continue
    else:
        print(f"You winner. You spend {trys} trys")
        break
