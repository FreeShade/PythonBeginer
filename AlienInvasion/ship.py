import pygame

class Ship:
    """клас для керування кораблем"""

    def __init__(self, ai_game):
        """ініціалізувати корабель та його стартову позицію"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # завантажити зображення корабля та отримати його рект
        self.image = pygame.image.load('C:/Users/Natrix/Desktop/repositories/PythonBeginer/AlienInvasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        #створювати кожен новий корабель внизу екрана , по центру.abs
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """намалювати корабель у його поточному розташування"""
        self.screen.blit(self.image, self.rect)