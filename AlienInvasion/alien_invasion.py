# import sys
# import pygame

# class AlienInvasion:
#     """Загальний клас що керує ресурсами"""

#     def __init__(self):

#         """ініціалізуємо гру"""
#         pygame.init()

#         self.screen = pygame.display.set_mode((1200, 800))
#         pygame.display.set_caption("Alien Invansion")

#     def run_game(self):
#         """розпочати головний цикл гри"""
#         while True:
#             # слідкувати за подіями миші і клавіатури
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     sys.exit()
            
#             #Показати останій намальований екран.
#             pygame.display.flip()

# if  __name__ == '__main__':
#     #створити екземпляр гри та запустити гру.
#     ai = AlienInvasion()
#     ai.run_game()

import sys
import pygame

class AlienInvasion:
    """Загальний клас що керує ресурсами"""

    def __init__(self):
        """ініціалізуємо гру"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")  

        #Задати колір фону
        self.bg_color = (34, 139, 34)

    def run_game(self):
        """розпочати головний цикл гри"""
        while True:
            # слідкувати за подіями миші і клавіатури
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
                #Наново перемальовувати екран на кожній ітерації  циклу
                self.screen.fill(self.bg_color)


                #Показати останній намальований екран.
                #self.screen.fill((230, 230, 230))  # додано заповнення екрану кольором
                pygame.display.flip()

if __name__ == '__main__':
    #створити екземпляр гри та запустити гру.
    ai = AlienInvasion()
    ai.run_game()