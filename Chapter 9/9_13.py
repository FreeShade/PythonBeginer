# Зробіть клас Dice з одним атрибутои, еапишіть метод щоб кидати кубик.
import random


class Dice:
    """Моделюємо гральний кубик"""

    def __init__(self, side):
        self.side = side

    def get_side(self):
        """Кинути кубик отримати сторону"""
        drop_dice = random.randint(1, self.side)
        return drop_dice

    def show_dice(self):
        """Показати скільки сторін в кубику."""
        explain = f"The dice have {self.side} sides"
        return explain

    def drop_dice(self):
        """Кидаємо кубик 10 разів."""
        for drop in range(10):
            print(f"You get {self.get_side()} on your dice.")


# визначаємо кубики.
dice_6 = Dice(6)
dice_10 = Dice(10)
dice_20 = Dice(20)


# Кидаємо кубики по 10 разів.
dice_6.drop_dice()
print("\n")
dice_10.drop_dice()
print("\n")
dice_20.drop_dice()


# print(dice_6.show_dice())
