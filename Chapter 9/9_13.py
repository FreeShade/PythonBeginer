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


dice_6 = Dice(6)


for drop in range(10):
    print(f"You get {dice_6.get_side()} on your dice.")

# print(dice_6.show_dice())
