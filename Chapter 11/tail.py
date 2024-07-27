import pygame
import sys

# Ініціалізація Pygame
pygame.init()

# Встановлення розміру вікна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Мишячий хвіст")

# Колір
WHITE = (255, 255, 255)

# Початкові координати хвоста
tail = [(0, 0)] * 10

# Головний цикл програми
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Отримання позиції миші
    mouse_pos = pygame.mouse.get_pos()

    # Додавання поточної позиції миші до хвоста
    tail.pop(0)
    tail.append(mouse_pos)

    # Очистка екрану
    screen.fill((0, 0, 0))

    # Малювання хвоста
    for i, pos in enumerate(tail):
        pygame.draw.circle(screen, WHITE, pos, i)

    # Оновлення вікна
    pygame.display.flip()
