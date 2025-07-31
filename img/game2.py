import random
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Поймай меня, если сможешь")
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/бабочка3.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

running = True
while running:
    # Генерация случайного цвета фона
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Отображение бабочки
    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()